from django.urls                import path
from home                       import views
from django.contrib.auth        import views as auth_views

app_name = "home"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('co_post', views.confession_post_view, name='confession_post_view'),

    #auth views
    path('a/login', auth_views.LoginView.as_view(template_name="home/log_in.html"), name='log_in_view'),
    path('a/signup', views.sign_up_view, name='sign_up_view'),
    path('a/logout', views.log_out_view, name='log_out_view'),
]
