from django.contrib                 import admin
from uprofile.models                import FollowProfile, QuestionPost, AnswerPost


admin.site.register(QuestionPost)
admin.site.register(AnswerPost)
admin.site.register(FollowProfile)
