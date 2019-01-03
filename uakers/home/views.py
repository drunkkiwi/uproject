from django.shortcuts       import render, redirect
from .models                import Confessions
from .forms                 import SignUpForm, ConfessionsForm
from django.contrib.auth    import login, authenticate, logout
from django.core.paginator  import EmptyPage, PageNotAnInteger, Paginator
from django.http            import JsonResponse


# -------------- HOME VIEW / CONFESSION VIEW ----------------------------
def home_view(request):
    all_conf = Confessions.objects.all().order_by('-id')

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

# ---------------- CONFESSION UNIQUE VIEW ------------------
def confession_view(request, confession_slug):
    cookieset = 'viewed_confession' + confession_slug

    unique_confession = Confessions.objects.get(confession_slug=confession_slug)

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
        'unique_confession': unique_confession,
    }

    response = render(request, 'home/confession_view.html', context)
    response.set_cookie(cookieset, 'yes')
    return response


# ---------------- Upvote and downvote confession views -----------------------
def upvote_view(request, confession_slug):

    upvote_confession = Confessions.objects.get(confession_slug=confession_slug)
    upvote_confession_author = upvote_confession.confession_author
    alert_message = False

    if request.user.is_authenticated:
        if not request.user == upvote_confession_author:
            if request.user in upvote_confession.confession_upvotes.all():
                upvote_confession.confession_upvotes.remove(request.user)
                upvote_confession.confession_upvotes_int -= 1
                upvote_confession.save()
                alert_message = "Unupvoted"
            else:
                upvote_confession.confession_upvotes.add(request.user)
                if request.user in upvote_confession.confession_downvotes.all():
                    upvote_confession.confession_downvotes.remove(request.user)
                    upvote_confession.confession_upvotes_int += 1
                upvote_confession.confession_upvotes_int += 1
                upvote_confession.save()
                alert_message = "Upvoted"

        else:
            alert_message = "Selfupvote"

    else:
        alert_message = "NotLogedIn"

    alert_upvote_int = upvote_confession.confession_upvotes_int

    data = {
        'alert_state': alert_message,
        'alert_upvote_state': alert_upvote_int
    }
    return JsonResponse(data)


def downvote_view(request, confession_slug):

    downvote_confession = Confessions.objects.get(confession_slug=confession_slug)
    downvote_confession_author = downvote_confession.confession_author
    alert_message = False

    if request.user.is_authenticated:
        if not request.user == downvote_confession_author:
            if request.user in downvote_confession.confession_downvotes.all():
                downvote_confession.confession_downvotes.remove(request.user)
                downvote_confession.confession_upvotes_int += 1
                downvote_confession.save()
                alert_message = "Undownvoted"
            else:
                downvote_confession.confession_downvotes.add(request.user)
                if request.user in downvote_confession.confession_upvotes.all():
                    downvote_confession.confession_upvotes.remove(request.user)
                    downvote_confession.confession_upvotes_int -= 1
                downvote_confession.confession_upvotes_int -= 1
                downvote_confession.save()
                alert_message = "Downvoted"
        else:
            alert_message = "Selfupvote"

    else:
        alert_message = "NotLoggedIn"

    alert_upvote_int = downvote_confession.confession_upvotes_int

    data = {
        'alert_state': alert_message,
        'alert_upvote_state': alert_upvote_int
    }
    return JsonResponse(data)


# ------------ AUTHENTICATION VIEWS ------------------------

#-------------- LOGIN VIEW ---------------------------------

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
