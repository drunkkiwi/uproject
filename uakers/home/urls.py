from django.urls                import path
from home                       import views
from django.contrib.auth        import views as auth_views

app_name = "home"

urlpatterns = [

    # ------------------- home ------------------------
    path('', views.home_view, name="home_view"),
    #---------------- post confession --------------------
    path('co_post', views.confession_post_view, name='confession_post_view'),
    # ----------------unique confession page --------------
    path('confession/<str:confession_slug>', views.confession_view, name='confession_view'),
    path('delete/confession/<str:confession_slug>', views.ConfessionDeleteView.as_view(), name='confession_delete_view'),


    # ------------------ confession upvote / downvote ---------------------
    path('u/<str:co_type>/<str:co_slug>', views.upvote_view, name='upvote_view'),
    path('d/<str:co_type>/<str:co_slug>', views.downvote_view, name='downvote_view'),


    # ---------------- auth views --------------------
    path('a/login', auth_views.LoginView.as_view(template_name="home/log_in.html"), name='log_in_view'),
    path('a/signup', views.sign_up_view, name='sign_up_view'),
    path('a/logout', views.log_out_view, name='log_out_view'),
]
