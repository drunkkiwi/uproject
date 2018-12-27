from django.shortcuts       import render, redirect
from .models                import Confessions
from .forms                 import SignUpForm, ConfessionsForm
from django.contrib.auth    import login, authenticate, logout


# -------------- HOME VIEW ----------------------------
def home_view(request):
    all_conf = Confessions.objects.all().order_by('-id')

    co_form = ConfessionsForm()

    context = {
        'all_conf': all_conf,
        'co_form': co_form,
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
