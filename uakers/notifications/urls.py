from django.urls                import path
from notifications              import views

app_name = "notifications"

urlpatterns = [
    # --------------------------- fetch live --------------------------------
    path('live_notification_list_view', views.live_notification_list_view, name='live_notification_list_view'),

    # ------------------------- read notifications -----------------------
    path('read_notification_list_view', views.read_notification_list_view, name='read_notification_list_view'),
]
