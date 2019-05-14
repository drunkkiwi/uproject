from django.urls                import path
from usearch                    import views

app_name = "usearch"

urlpatterns = [
    # ----------------------- search views ---------------------------
    path('', views.search_view, name='search_view')
]
