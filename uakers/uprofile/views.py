from django.shortcuts                   import render, redirect, get_object_or_404
from home.models                        import UserProfile
from uprofile.models                    import QuestionPost, AnswerPost, FollowProfile
from home.models                        import Confessions
from django.contrib.auth.decorators     import login_required
from itertools                          import chain
from operator                           import attrgetter
from django.urls                        import reverse_lazy
from django.views.generic.edit          import DeleteView



# -------------------------------- PROFILE PAGE --------------------------------------
def profile_view(request, profile_slug=''):

    isuser = False
    have_followed_them = False

    if profile_slug == '':
        if request.user.is_authenticated:
            isuser = True
            profile_slug = request.user.profile_slug
        else:
            return redirect('home:home_view')

    user_profile = UserProfile.objects.get(profile_slug=profile_slug)
    user_confession_number = Confessions.objects.filter(confession_author=user_profile).count()

    if FollowProfile.objects.filter(follow_init=request.user, follow_rec=user_profile).exists():
        have_followed_them = True

    fo_nr = FollowProfile.objects.filter(follow_rec=user_profile).count()
    following_nr = FollowProfile.objects.filter(follow_init=user_profile).count()


    user_questions = QuestionPost.objects.filter(question_directed=user_profile).all()
    user_confessions = Confessions.objects.filter(confession_author=user_profile).all()
    # descending order
    user_posts = sorted(
        chain(user_questions, user_confessions),
        key=attrgetter('date_created_at'),
        reverse=True)


    if user_profile == request.user:
        isuser = True

    context = {
        'user_posts': user_posts,
        'user_questions': user_questions,
        'user_profile': user_profile,
        'user_confession_number': user_confession_number,
        'isuser': isuser,
        'have_followed_them': have_followed_them,
        'fo_nr': fo_nr,
        'following_nr': following_nr,
    }
    return render(request, 'uprofile/profile_view.html', context)



# ------------------------- Delete question / answers --------------------------
class QuestionDeleteView(DeleteView):
    model = Confessions
    success_url = reverse_lazy('uprofile:profile_view')

    def get_object(self):
        object = get_object_or_404(QuestionPost, question_slug=self.kwargs['question_slug'])
        return object



# ------------------------- Follow profile --------------------------------------
def follow_profile_view(request, init_profile_slug, rec_profile_slug):

    init_profile = UserProfile.objects.get(profile_slug=init_profile_slug)
    rec_profile = UserProfile.objects.get(profile_slug=rec_profile_slug)

    if not FollowProfile.objects.filter(follow_init=init_profile, follow_rec=rec_profile).exists():
        FollowProfile.objects.create(follow_init=init_profile, follow_rec=rec_profile)
        return redirect('uprofile:profile_view')
    else:
        return redirect('uprofile:profile_view')

    return redirect('uprofile:profile_view')
