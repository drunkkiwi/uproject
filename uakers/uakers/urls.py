from django.contrib         import admin
from django.urls            import path, include

urlpatterns = [

    # ------- home app ----------
    path('', include('home.urls')),
    # -------- uprofile app ---------
    path('profile/', include('uprofile.urls')),
    # ------- notification app ----------
    path('notifications/', include('notifications.urls')),
    # ------- usearch app ------------
    path('search/', include('usearch.urls')),

    # --------- admin ------------
    path('admin/', admin.site.urls),
]
