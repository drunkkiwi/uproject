from django.shortcuts import render
from home.models import UserProfile
from home.models import Confessions


def profile_view(request, profile_slug=''):

    if profile_slug == '':
        profile_slug = request.user.profile_slug

    user_profile = UserProfile.objects.get(profile_slug=profile_slug)
    user_confession_number = Confessions.objects.filter(confession_author=user_profile).count()

    context = {
        'user_profile': user_profile,
        'user_confession_number': user_confession_number,
    }
    return render(request, 'uprofile/profile_view.html', context)
