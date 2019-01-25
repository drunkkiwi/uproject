from django             import template
from home.models        import UserProfile
from uprofile.models    import FollowProfile

register = template.Library()


@register.filter(name='rec_followed_by')
def rec_followed_by(follow_user):
    return FollowProfile.objects.filter(follow_rec=follow_user).count()


@register.filter(name='rec_following')
def rec_following(follow_user):
    return FollowProfile.objects.filter(follow_init=follow_user).count()
