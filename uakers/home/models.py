from django.template.defaultfilters     import slugify
from django.contrib.auth.models         import User, AbstractUser
from django.db.models.signals           import post_save
from django.dispatch                    import receiver
from django.db                          import models
from .choices                           import *
from .external_functions                import CustomUsernameValidator

# -------------------------- CUSTOM USER PROFILE ------------------------------
class UserProfile(AbstractUser):
    profile_nickname        = models.CharField(max_length=35)
    profile_year            = models.CharField(max_length=2, choices=YCHOICES)
    profile_sex             = models.CharField(max_length=1, choices=SCHOICES)
    profile_image           = models.CharField(max_length=700, blank=True)
    profile_slug            = models.SlugField(blank=True, max_length=900, unique=True)
    profile_song            = models.CharField(max_length=300, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        self._meta.get_field(
            'username'
        ).validators[0] = CustomUsernameValidator()

        super().__init__(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.profile_nickname:
            self.profile_nickname = self.username


        if self.profile_song:
            if self.profile_song[:5] == 'https':
                self.profile_song = 'https://www.youtube.com/embed/' + str(self.profile_song[32:])
            elif self.profile_song[:5] == 'http:':
                self.profile_song = 'https://www.youtube.com/embed/' + str(self.profile_song[31:])
            elif self.profile_song[:3] == 'www':
                self.profile_song = 'https://www.youtube.com/embed/' + str(self.profile_song[24:])

        cusername = self.username

        if not self.id:
            if UserProfile.objects.filter(profile_slug=slugify(cusername)).exists():
                count = UserProfile.objects.filter(profile_slug__startswith=slugify(cusername)).exclude(pk=self.id).count()
                self.profile_slug = slugify(cusername + str(count))
            else:
                self.profile_slug = slugify(cusername)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.username + ', ' + self.profile_year + ', ' + self.profile_sex



#--------------------------- CONFESSIONS -----------------------------
class Confessions(models.Model):
    confession_author       = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    confession_title        = models.CharField(max_length=100)
    confession_body         = models.TextField(blank=False, null=False)
    confession_upvotes      = models.ManyToManyField(UserProfile, related_name='confession_upvotes', blank=True)
    confession_downvotes    = models.ManyToManyField(UserProfile, related_name='confession_downvotes', blank=True)
    confession_upvotes_int  = models.IntegerField(default=0)
    confession_views        = models.IntegerField(default=0)
    date_created_at         = models.DateTimeField(auto_now_add=True)
    confession_updated_at   = models.DateTimeField(auto_now=True)
    confession_slug         = models.SlugField(blank=True, max_length=900)

    def save(self, *args, **kwargs):
        cbody = self.confession_body[:60]

        if not self.id:
            if Confessions.objects.filter(confession_slug=slugify(cbody)).exists():
                count = Confessions.objects.filter(confession_slug__startswith=slugify(cbody)).exclude(pk=self.id).count()
                self.confession_slug = slugify(cbody + str(count))
            else:
                self.confession_slug = slugify(cbody)
        super(Confessions, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.confession_author.username) + ', ' + str(self.confession_title) + ', ' + str(self.confession_upvotes_int)



# ---------------------- CONFESSION COMMENTS ----------------------------
class ConfessionComment(models.Model):
    comment_confession      = models.ForeignKey(Confessions, on_delete=models.CASCADE)
    comment_author          = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment_body            = models.TextField(blank=False, null=False)
    comment_created_at      = models.DateTimeField(auto_now_add=True)
    comment_upvotes_int     = models.IntegerField(default=0)
    comment_upvotes         = models.ManyToManyField(UserProfile, related_name='comment_upvotes', blank=True)
    comment_downvotes       = models.ManyToManyField(UserProfile, related_name='comment_downvotes', blank=True)
    comment_slug            = models.SlugField(blank=True, max_length=900)

    def save(self, *args, **kwargs):
        cbody = self.comment_body[:50]

        if not self.id:
            if ConfessionComment.objects.filter(comment_slug=slugify(cbody)).exists():
                count = ConfessionComment.objects.filter(comment_slug__startswith=slugify(cbody)).exclude(pk=self.id).count()
                self.comment_slug = slugify(cbody + str(count))
            else:
                self.comment_slug = slugify(cbody)
        super(ConfessionComment, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.comment_body) + ', ' + str(self.comment_upvotes_int)
