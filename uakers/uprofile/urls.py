from django.urls                import path
from uprofile                   import views
from django.contrib.auth        import views as auth_views

app_name = "uprofile"

urlpatterns = [
    # ----------------------- profile views ---------------------------
    path('<str:profile_slug>', views.profile_view, name='profile_view'),
    path('', views.profile_view, name='profile_view'),

    # -------------------- delete quesiton --- answer ------------------
    path('delete/question/<str:question_slug>', views.QuestionDeleteView.as_view(), name='question_delete_view'),

    # ------------------------ Follow view -----------------------------
    path('follow/<str:init_profile_slug>/<str:rec_profile_slug>', views.follow_profile_view, name='follow_profile_view'),
]
