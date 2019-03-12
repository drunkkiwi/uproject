from django.shortcuts           import render, redirect, get_object_or_404
from .models                    import Confessions, ConfessionComment
from .forms                     import SignUpForm, ConfessionsForm, ConfessionCommentForm
from django.contrib.auth        import login, authenticate, logout
from django.core.paginator      import EmptyPage, PageNotAnInteger, Paginator
from django.http                import JsonResponse
from django.urls                import reverse_lazy
from django.views.generic.edit  import DeleteView
from notifications.models       import Notification



# -------------- HOME VIEW / CONFESSION VIEW ----------------------------
def home_view(request):
    all_conf = Confessions.objects.all().order_by('-id')[:100]

    co_form = ConfessionsForm()

    paginator = Paginator(all_conf, 20)

    page = request.GET.get('page')
    paginated = paginator.get_page(page)
    pg_number = []

    for post in paginated:
        pg_number.append(post)

    pg_nr_odd = False;
    pg_number = len(pg_number)
    if (pg_number%2) is 0:
        pg_nr_odd = False
    else:
        pg_nr_odd = True


    context = {
        'all_conf': paginated,
        'co_form': co_form,
        'pg_nr_odd': pg_nr_odd,
    }
    return render(request, 'home/home.html', context)

# ------------- CONFESSION POST FORM VIEW -----------------
def confession_post_view(request):
    co_form = ConfessionsForm(request.POST)
    if co_form.is_valid():
        temp = co_form.save(commit=False)
        temp.confession_author = request.user
        temp.save()
        return redirect('home:home_view')

    return redirect('home:home_view')

# --------------- Confession delete view -----------------
class ConfessionDeleteView(DeleteView):
    model = Confessions
    success_url = reverse_lazy('home:home_view')

    def get_object(self):
        object = get_object_or_404(Confessions, confession_slug=self.kwargs['confession_slug'])
        return object


# ---------------- CONFESSION UNIQUE VIEW ------------------
def confession_view(request, confession_slug):
    cookieset = 'viewed_confession' + confession_slug

    unique_confession = Confessions.objects.get(confession_slug=confession_slug)
    all_confession_comments = ConfessionComment.objects.filter(comment_confession=unique_confession).order_by('-comment_upvotes_int')[:50]

    redirect_next_page = request.POST.get('next_page', '/')

    if request.method == 'GET':
        co_form = ConfessionCommentForm()
    elif request.method == 'POST':
        co_form = ConfessionCommentForm(request.POST)
        if co_form.is_valid():
            temp = co_form.save(commit=False)
            temp.comment_author = request.user
            temp.comment_confession = unique_confession
            temp.save()
            Notification.objects.create(notification_init=temp.comment_author, notification_rec=temp.comment_confession.confession_author, notification_type='commentConf', notification_target=temp.comment_confession.confession_slug)
            return redirect(redirect_next_page)

        return redirect('home:confession_view')


    if cookieset in request.COOKIES:
        if request.COOKIES[cookieset] == 'yes':
            pass
        else:
            unique_confession.confession_views += 1;
            unique_confession.save()
    else:
        unique_confession.confession_views += 1;
        unique_confession.save()

    context = {
        'cons': unique_confession,
        'all_confession_comments': all_confession_comments,
        'co_form': co_form,
    }

    response = render(request, 'home/confession_view.html', context)
    response.set_cookie(cookieset, 'yes')
    return response


# ---------------- Upvote and downvote confession views -----------------------
def upvote_view(request, co_type, co_slug):

    alert_upvote_int = False
    alert_message = False
    upvote_co = False

    if request.user.is_authenticated:

        if co_type == 'confession':
            upvote_co = Confessions.objects.get(confession_slug=co_slug)
            if request.user in upvote_co.confession_upvotes.all():
                upvote_co.confession_upvotes.remove(request.user)
                upvote_co.confession_upvotes_int -= 1
                upvote_co.save()
                alert_message = "Unupvoted"
            else:
                upvote_co.confession_upvotes.add(request.user)
                if request.user in upvote_co.confession_downvotes.all():
                    upvote_co.confession_downvotes.remove(request.user)
                    upvote_co.confession_upvotes_int += 1
                upvote_co.confession_upvotes_int += 1
                upvote_co.save()
                alert_message = "Upvoted"
                notification_slug = str(upvote_co.confession_slug)
                if not request.user == upvote_co.confession_author:
                    Notification.objects.create(notification_init=request.user, notification_rec=upvote_co.confession_author, notification_type='likeConf', notification_target=notification_slug)

            alert_upvote_int = upvote_co.confession_upvotes_int

        elif co_type == 'comment':
            upvote_co = ConfessionComment.objects.get(comment_slug=co_slug)

            if request.user in upvote_co.comment_upvotes.all():
                upvote_co.comment_upvotes.remove(request.user)
                upvote_co.comment_upvotes_int -= 1
                upvote_co.save()
                alert_message = "Unupvoted"
            else:
                upvote_co.comment_upvotes.add(request.user)
                if request.user in upvote_co.comment_downvotes.all():
                    upvote_co.comment_downvotes.remove(request.user)
                    upvote_co.comment_upvotes_int += 1
                upvote_co.comment_upvotes_int += 1
                upvote_co.save()
                alert_message = "Upvoted"

                notification_slug = str(upvote_co.comment_confession.confession_slug)
                if not request.user == upvote_co.comment_author:
                    Notification.objects.create(notification_init=request.user, notification_rec=upvote_co.comment_author, notification_type='likeCom', notification_target=notification_slug)

            alert_upvote_int = upvote_co.comment_upvotes_int


    else:
        alert_message = "NotLoggedIn"


    data = {
        'alert_state': alert_message,
        'alert_upvote_state': alert_upvote_int,
    }
    return JsonResponse(data)


def downvote_view(request, co_type, co_slug):

    alert_upvote_int = False
    alert_message = False
    downvote_co = False

    if request.user.is_authenticated:

        if co_type == 'confession':

            downvote_co = Confessions.objects.get(confession_slug=co_slug)

            if request.user in downvote_co.confession_downvotes.all():
                downvote_co.confession_downvotes.remove(request.user)
                downvote_co.confession_upvotes_int += 1
                downvote_co.save()
                alert_message = "Undownvoted"
            else:
                downvote_co.confession_downvotes.add(request.user)
                if request.user in downvote_co.confession_upvotes.all():
                    downvote_co.confession_upvotes.remove(request.user)
                    downvote_co.confession_upvotes_int -= 1
                downvote_co.confession_upvotes_int -= 1
                downvote_co.save()
                alert_message = "Downvoted"

            alert_upvote_int = downvote_co.confession_upvotes_int

        elif co_type == 'comment':

            downvote_co = ConfessionComment.objects.get(comment_slug=co_slug)

            if request.user in downvote_co.comment_downvotes.all():
                downvote_co.comment_downvotes.remove(request.user)
                downvote_co.comment_upvotes_int += 1
                downvote_co.save()
                alert_message = "Undownvoted"
            else:
                downvote_co.comment_downvotes.add(request.user)
                if request.user in downvote_co.comment_upvotes.all():
                    downvote_co.comment_upvotes.remove(request.user)
                    downvote_co.comment_upvotes_int -= 1
                downvote_co.comment_upvotes_int -= 1
                downvote_co.save()
                alert_message = "Downvoted"

                alert_upvote_int = downvote_co.comment_upvotes_int

        else:
            return false

    else:
        alert_message = "NotLoggedIn"


    data = {
        'alert_state': alert_message,
        'alert_upvote_state': alert_upvote_int
    }
    return JsonResponse(data)


# ------------ AUTHENTICATION VIEWS ------------------------

# ---------------- SIGN UP VIEW ----------------------------
def sign_up_view(request):
    if not request.user.is_authenticated:
        sign_up_btn = 'Sign up'
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home:home_view')
        else:
            form = SignUpForm()
    else:
        return redirect('home:home_view');

    context = {
        'form': form,
        'sign_up_btn': sign_up_btn,
    }
    return render(request, 'home/sign_up.html', context)



#------------------- LOG OUT VIEW ------------------------
def log_out_view(request):
    logout(request)
    return redirect('home:log_in_view')
