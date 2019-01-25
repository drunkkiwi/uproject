from django.urls                import path
from uprofile                   import views
from django.contrib.auth        import views as auth_views

app_name = "uprofile"

urlpatterns = [
    # ----------------------- profile views ---------------------------
    path('<slug:profile_slug>', views.profile_view, name='profile_view'),
    path('', views.profile_view, name='profile_view'),

    # -------------------- delete quesiton --- answer ------------------
    path('delete/question/<slug:question_slug>', views.QuestionDeleteView.as_view(), name='question_delete_view'),

    # ------------------------ Follow function view -----------------------------
    path('follow/<slug:init_profile_slug>/<slug:rec_profile_slug>', views.follow_profile_view, name='follow_profile_view'),

    # ------------------- Followed / Following page view --------------------
    path('followed/<slug:profile_slug>', views.followed_view, name='followed_view'),
    path('following/<slug:profile_slug>', views.following_view, name='following_view'),
]
