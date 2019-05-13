from django.shortcuts                               import render
from .models                                        import Notification
from django.http                                    import JsonResponse
from django.forms.models                            import model_to_dict
from django.core                                    import serializers
from django.urls                                    import reverse
from django.contrib.humanize.templatetags.humanize  import naturaltime




def live_notification_list_view(request):

    # --------------- notification list and notification number ----------------------
    live_notification_list = Notification.objects.filter(notification_rec=request.user, notification_recieved=False).all()

    live_notification_count = Notification.objects.filter(notification_rec=request.user, notification_read=False).count()

    # --------------------------- notification list array ---------------------------
    live_notification_array = []

    # ------------------------ notification structure -----------------------------
    for notification in live_notification_list:
        if notification.notification_recieved == False:
            notification.notification_recieved = True
            notification.save()

        struct = model_to_dict(notification)
        if notification.notification_init:
            struct['notification_init'] = str(notification.notification_init.username)
            struct['notification_image'] = str(notification.notification_init.profile_image)
            if notification.notification_type == 'follow':
                struct['notification_url'] = reverse('uprofile:profile_view') + '/' + str(notification.notification_init.profile_slug)
            elif notification.notification_type == 'likeConf':
                struct['notification_url'] = reverse('home:confession_view', args=[notification.notification_target])
            elif notification.notification_type == 'likeCom':
                struct['notification_url'] = reverse('home:confession_view', args=[notification.notification_target])
            elif notification.notification_type == 'commentConf':
                struct['notification_url'] = reverse('home:confession_view', args=[notification.notification_target])

        if notification.notification_type:
            struct['notification_type'] = str(notification.notification_type)
        if notification.notification_created_at:
            struct['notification_created_at'] = str(naturaltime(notification.notification_created_at))

        live_notification_array.append(struct)


    data = {
        'live_notification_list': live_notification_array,
        'live_notification_count': live_notification_count,
    }

    return JsonResponse(data)


def read_notification_list_view(request):

    all_req_notifications = Notification.objects.filter(notification_rec=request.user, notification_read=False)

    func_status = 'Done'


    for notification in all_req_notifications:
        notification.notification_read = True
        notification.save()



    data = {
        'func_status': func_status,
    }

    return JsonResponse(data)
