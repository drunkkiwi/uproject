from django.contrib import admin
from .models import UserProfile, Confessions, ConfessionComment

admin.site.register(UserProfile)
admin.site.register(Confessions)
admin.site.register(ConfessionComment)
