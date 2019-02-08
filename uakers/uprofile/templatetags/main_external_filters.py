from django                 import template
from home.models            import UserProfile
from uprofile.models        import FollowProfile
from notifications.models   import Notification

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


@register.simple_tag()
def get_notification_number(user):
    return Notification.objects.filter(notification_rec=user, notification_read=False, notification_sent=False).count()



@register.simple_tag()
def get_notification_list(user):
    notifications = Notification.objects.filter(notification_rec=user).order_by('-id')[:10]
    for notification in notifications:
        notification.notification_sent = True
        notification.save()
    return notifications
