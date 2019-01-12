from django.urls                import path
from uprofile                   import views
from django.contrib.auth        import views as auth_views

app_name = "uprofile"

urlpatterns = [
    path('<str:profile_slug>', views.profile_view, name='profile_view'),
    path('', views.profile_view, name='profile_view'),
]
