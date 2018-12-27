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
    confession_author       = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    confession_title        = models.CharField(max_length=100)
    confession_body         = models.TextField(blank=False, null=False)
    confession_upvotes      = models.IntegerField(default=0)
    confession_views        = models.IntegerField(default=0)
    confession_created_at   = models.DateTimeField(auto_now_add=True)
    confession_updated_at   = models.DateTimeField(auto_now=True)
    confession_slug         = models.SlugField(blank=True, max_length=900)

    def save(self, *args, **kwargs):
        ctitle = self.confession_title

        if not self.id:
            if Confession.objects.filter(confession_slug=slugify(ctitle)).exists():
                count = Confession.objects.filter(confession_slug__startswith=slugify(ctitle)).exclude(pk=self.id).count()
                self.confession_slug = slugify(ctitle + str(count))
            else:
                self.confession_slug = slugify(ctitle)
        super(Confessions, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.confession_author.username) + ', ' + str(self.confession_title) + ', ' + str(self.confession_upvotes)
