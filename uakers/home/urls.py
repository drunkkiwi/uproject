from django.urls                import path
from home                       import views

app_name = "home"

urlpatterns = [
    path('', views.home_view, name="home_view"),
]