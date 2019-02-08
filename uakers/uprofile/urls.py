from django.urls                import path
from uprofile                   import views
from django.contrib.auth        import views as auth_views

app_name = "uprofile"

urlpatterns = [
    # ----------------------- profile views ---------------------------
    path('v/<slug:profile_slug>', views.profile_view, name='profile_view'),
    path('v', views.profile_view, name='profile_view'),

    # ---------------------------- edit profile ------------------------------
    path('update', views.UserProfileUpdate.as_view(), name='user_profile_update_view'),

    # ---------------------- post question --- naswer -------------------
    path('post/question/<slug:rec_profile_slug>', views.question_post_view, name='question_post_view'),
    path('post/answer/<slug:question_instance_slug>', views.answer_post_view, name='answer_post_view'),

    # -------------------- delete question --- answer ------------------
    path('delete/question/<slug:question_slug>', views.QuestionDeleteView.as_view(), name='question_delete_view'),

    # ------------------------ Follow function view -----------------------------
    path('follow/<slug:rec_profile_slug>', views.follow_profile_view, name='follow_profile_view'),

    # ------------------- Followed / Following page view --------------------
    path('followed/<slug:profile_slug>', views.followed_view, name='followed_view'),
    path('following/<slug:profile_slug>', views.following_view, name='following_view'),

]
