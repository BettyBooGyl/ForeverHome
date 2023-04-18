from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE, related_name="reciver")
    message = models.CharField(max_length=500)
    date_and_time_sent = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)