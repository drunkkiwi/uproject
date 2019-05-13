from django                 import template
from notifications.models   import Notification

register = template.Library()
# ---------------------------------- Notification tags ---------------------------------
@register.simple_tag()
def get_notification_number(user):
    return Notification.objects.filter(notification_rec=user, notification_read=False).count()



@register.simple_tag()
def get_notification_list(user):
    notifications = Notification.objects.filter(notification_rec=user).order_by('-id')[:5]
    return notifications
