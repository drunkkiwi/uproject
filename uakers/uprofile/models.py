from django.template.defaultfilters     import slugify
from django.db                          import models
from home.models                        import UserProfile




# ---------------------------- Follow model ----------------------------
class FollowProfile(models.Model):
    follow_init             = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follow_init')
    follow_rec              = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follow_rec')
    follow_created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.follow_init) + ', ' + str(self.follow_rec) + ', ' + str(self.follow_created_at)



# ------------------------------ Question model --------------------------------
class QuestionPost(models.Model):
    question_author             = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author_question')
    question_directed          = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reciever_question')
    question_body              = models.TextField(blank=False, null=False)
    date_created_at            = models.DateTimeField(auto_now_add=True)
    question_slug              = models.SlugField(blank=True, max_length=900)


    def save(self, *args, **kwargs):
        cbody = self.question_body[:30]

        if not self.id:
            if QuestionPost.objects.filter(question_slug=slugify(cbody)).exists():
                count = QuestionPost.objects.filter(question_slug__startswith=slugify(cbody)).exclude(pk=self.id).count()
                self.question_slug = slugify(cbody + str(count))
            else:
                self.question_slug = slugify(cbody)
        super(QuestionPost, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.question_author) + ', ' + str(self.question_directed) + ', ' + str(self.date_created_at)


# ------------------------------- Anser model ----------------------------------
class AnswerPost(models.Model):
    answer_question          = models.ForeignKey(QuestionPost, on_delete=models.CASCADE)
    answer_author            = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    answer_body              = models.TextField(blank=False, null=False)
    answer_created_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.answer_question) + ', ' + str(self.answer_body)
