from django.db import models
from django.utils import timezone

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE, related_name="sender", to_field='username')
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    message = models.CharField(max_length=500)
    date_and_time_sent = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.message

class Notification(models.Model):
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    user = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username