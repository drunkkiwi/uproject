from django.contrib         import admin
from django.urls            import path, include

urlpatterns = [

    # ------- home app ----------
    path('', include('home.urls')),

    # -------- uprofile app ---------
    path('profile/', include('uprofile.urls')),

    # --------- admin ------------
    path('admin/', admin.site.urls),
]
