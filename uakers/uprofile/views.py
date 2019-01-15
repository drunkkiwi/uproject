from django.shortcuts                   import render, redirect
from home.models                        import UserProfile
from uprofile.models                    import QuestionPost
from home.models                        import Confessions
from django.contrib.auth.decorators     import login_required
from itertools                          import chain
from operator                           import attrgetter


def profile_view(request, profile_slug=''):

    isuser = False
    if profile_slug == '':
        if request.user.is_authenticated:
            isuser = True
            profile_slug = request.user.profile_slug
        else:
            return redirect('home:home_view')

    user_profile = UserProfile.objects.get(profile_slug=profile_slug)
    user_confession_number = Confessions.objects.filter(confession_author=user_profile).count()


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
    }
    return render(request, 'uprofile/profile_view.html', context)
