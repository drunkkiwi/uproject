from django.urls                import path
from home                       import views
from django.contrib.auth        import views as auth_views

app_name = "home"

urlpatterns = [

    # ------------------- home ------------------------
    path('', views.home_view, name="home_view"),
    #---------------- post confession --------------------
    path('co_post', views.confession_post_view, name='confession_post_view'),
    #----------------unique confession page --------------
    path('confession/<str:confession_slug>', views.confession_view, name='confession_view'),


    # ------------------ post upvote / downvote ---------------------
    path('u/<str:confession_slug>', views.upvote_view, name='upvote_view'),
    path('d/<str:confession_slug>', views.downvote_view, name='downvote_view'),

    # ---------------- auth views --------------------
    path('a/login', auth_views.LoginView.as_view(template_name="home/log_in.html"), name='log_in_view'),
    path('a/signup', views.sign_up_view, name='sign_up_view'),
    path('a/logout', views.log_out_view, name='log_out_view'),
]
