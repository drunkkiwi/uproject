from django.template.defaultfilters     import slugify
from django.contrib.auth.models         import User, AbstractUser
from django.db.models.signals           import post_save
from django.dispatch                    import receiver
from django.db                          import models
from .choices                           import *


class UserProfile(AbstractUser):

    profile_year        = models.CharField(max_length=2, choices=YCHOICES)
    profile_sex         = models.CharField(max_length=1, choices=SCHOICES)
    profile_image       = models.CharField(max_length=700, blank=True)

    def __str__(self):
        return self.username + ', ' + self.profile_year + ', ' + self.profile_sex


class Confessions(models.Model):
    confession_author  = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    confession_title   = models.CharField(max_length=100)
    confession_body    = models.TextField(blank=False, null=False)
    confession_upvotes = models.IntegerField(default=0)
    confession_views   = models.IntegerField(default=0)


    def __str__(self):
        return str(self.confession_author.username) + ', ' + str(self.confession_title) + ', ' + str(self.confession_upvotes)
