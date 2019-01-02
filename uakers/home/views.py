from django.shortcuts       import render, redirect
from .models                import Confessions
from .forms                 import SignUpForm, ConfessionsForm
from django.contrib.auth    import login, authenticate, logout
from django.core.paginator  import EmptyPage, PageNotAnInteger, Paginator


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

# ------------ AUTHENTICATION VIEWS ------------------------

#-------------- LOGIN VIEW ---------------------------------

# ---------------- SIGN UP VIEW ----------------------------
def sign_up_view(request):
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

    context = {
        'form': form,
        'sign_up_btn': sign_up_btn,
    }
    return render(request, 'home/sign_up.html', context)



#------------------- LOG OUT VIEW ------------------------
def log_out_view(request):
    logout(request)
    return redirect('home:home_view')
