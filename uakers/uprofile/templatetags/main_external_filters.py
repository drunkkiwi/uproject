from django             import template
from home.models        import UserProfile
from uprofile.models    import FollowProfile

register = template.Library()


@register.filter(name='m_or_f_color')
def m_or_f_color(user_profile):
    morf = False
    if user_profile.profile_sex is 'M':
        morf = 'lmi-m'
    elif user_profile.profile_sex is 'F':
        morf = 'lmi-f'
    else:
        morf = ''

    return morf
