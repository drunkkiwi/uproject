from django.urls                import path
from home                       import views
from django.contrib.auth        import views as auth_views

app_name = "home"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('co_post', views.confession_submit, name='co_post'),

    #auth views
    path('a/register', views.register, name='register'),
    path('a/logout', auth_views.LogoutView.as_view(next_page="/"), name='log_out'),
]
