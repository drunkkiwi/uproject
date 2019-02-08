from django.urls                import path
from notifications              import views

app_name = "notifications"

urlpatterns = [
    path('live_notification_list_view', views.live_notification_list_view, name='live_notification_list_view'),
]
