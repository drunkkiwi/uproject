from django.shortcuts                   import render, redirect, get_object_or_404
from home.models                        import UserProfile
from uprofile.models                    import QuestionPost, AnswerPost, FollowProfile
from home.models                        import Confessions
from django.contrib.auth.decorators     import login_required
from itertools                          import chain
from operator                           import attrgetter
from django.urls                        import reverse_lazy
from django.views.generic.edit          import DeleteView
from .forms                             import QuestionPostForm, AnswerPostForm



# -------------------------------- PROFILE PAGE --------------------------------------
def profile_view(request, profile_slug=''):

    # --------- initial variables -------
    isuser = False
    have_followed_them = False

    # ----------- if user is authenticated then see if it is requests user -----------
    if profile_slug == '':
        if request.user.is_authenticated:
            isuser = True
            profile_slug = request.user.profile_slug
        else:
            return redirect('home:home_view')


    # --------------------------- FIND THE USER PROFILE -----------------------------------
    user_profile = UserProfile.objects.get(profile_slug=profile_slug)
    user_confession_number = Confessions.objects.filter(confession_author=user_profile).count()

    # ---------------------- if there is user and they have followed ----------------------------
    if request.user.is_authenticated:
        if FollowProfile.objects.filter(follow_init=request.user, follow_rec=user_profile).exists():
            have_followed_them = True


    # --------------------------------- All posts ----------------------------------
    user_questions = QuestionPost.objects.filter(question_directed=user_profile).all()
    user_confessions = Confessions.objects.filter(confession_author=user_profile).all()


    # --------------------- Coupled together and sorted posts ---------------------
    user_posts = sorted(
        chain(user_questions, user_confessions),
        key=attrgetter('date_created_at'),
        reverse=True)


    # ------------------------------- is req.user the profile? -------------------------
    if user_profile == request.user:
        isuser = True

    # ------------------------ QuestionPost and AnswerPost forms ----------------------
    if request.method == 'GET':
        qu_form = QuestionPostForm()
        ans_form = AnswerPostForm()

    context = {
        'user_posts': user_posts,
        'user_questions': user_questions,
        'user_profile': user_profile,
        'user_confession_number': user_confession_number,
        'isuser': isuser,
        'have_followed_them': have_followed_them,
        'qu_form': qu_form,
        'ans_form': ans_form,
    }
    return render(request, 'uprofile/profile_view.html', context)


# ------------------------------ Create question ---------------------------
def question_post_view(request, rec_profile_slug):
    redirect_next_page = request.POST.get('next_page', '/')
    rec_question_profile = UserProfile.objects.get(profile_slug=rec_profile_slug)
    qu_form = QuestionPostForm(request.POST)
    if request.method == 'POST':
        if qu_form.is_valid():
            temp = qu_form.save(commit=False)
            temp.question_author = request.user
            temp.question_directed = rec_question_profile
            temp.save()
            return redirect(redirect_next_page)

    return redirect('home:home_view')

def answer_post_view(request, question_instance_slug):
    redirect_next_page = request.POST.get('next_page', '/')
    question_instance = QuestionPost.objects.get(question_slug=question_instance_slug)
    ans_form = AnswerPostForm(request.POST)
    if request.method == 'POST':
        if ans_form.is_valid():
            temp = ans_form.save(commit=False)
            temp.answer_author = request.user
            temp.answer_question = question_instance
            temp.save()
            return redirect(redirect_next_page)

    return redirect('home:home_view')

# ------------------------- Delete question / answers --------------------------
class QuestionDeleteView(DeleteView):
    model = Confessions
    success_url = reverse_lazy('uprofile:profile_view')

    def get_object(self):
        object = get_object_or_404(QuestionPost, question_slug=self.kwargs['question_slug'])
        return object



# ------------------------- Follow profile --------------------------------------
@login_required
def follow_profile_view(request, init_profile_slug, rec_profile_slug):

    init_profile = UserProfile.objects.get(profile_slug=init_profile_slug)
    rec_profile = UserProfile.objects.get(profile_slug=rec_profile_slug)

    if not FollowProfile.objects.filter(follow_init=init_profile, follow_rec=rec_profile).exists():
        FollowProfile.objects.create(follow_init=init_profile, follow_rec=rec_profile)
        return redirect('uprofile:profile_view')
    else:
        FollowProfile.objects.filter(follow_init=init_profile, follow_rec=rec_profile).delete()

    return redirect('uprofile:profile_view')



# ------------------------- Followed /// Following views --------------------------
def followed_view(request, profile_slug):

    isuser = False
    user_profile = UserProfile.objects.get(profile_slug=profile_slug)

    if user_profile == request.user:
        isuser = True

    followed_by_profiles = FollowProfile.objects.filter(follow_rec=user_profile)

    context = {
        'user_profile': user_profile,
        'followed_by_profiles': followed_by_profiles,
        'isuser': isuser,
    }

    return render(request, 'uprofile/followed_view.html', context)



def following_view(request, profile_slug):

    isuser = False
    user_profile = UserProfile.objects.get(profile_slug=profile_slug)

    if user_profile == request.user:
        isuser = True

    following_profiles = FollowProfile.objects.filter(follow_init=user_profile)

    context = {
        'user_profile': user_profile,
        'following_profiles': following_profiles,
        'isuser': isuser,
    }

    return render(request, 'uprofile/following_view.html', context)
