from django.db                          import models
from home.models                        import UserProfile


# ------------------------- Notification model --------------------------

class Notification(models.Model):
    notification_init             = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notify_init')
    notification_rec              = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notify_rec')
    notification_type             = models.CharField(max_length=255)
    notification_target           = models.CharField(max_length=255, blank=True, null=True)
    notification_read             = models.BooleanField(default=False)
    notification_created_at       = models.DateTimeField(auto_now_add=True)
    notification_sent             = models.BooleanField(default=False)

    def __str__(self):
        return str(self.notification_init) + ', ' + str(self.notification_rec) + ', ' + str(self.notification_type)
