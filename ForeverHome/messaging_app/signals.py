from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    print("Got Here!")
    if created:
        channel_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(read=False, user=instance.user).count()
        print(notification_obj)
        user_id = str(instance.user.userID)
        print(user_id)
        print("This is from the signal")
        data = {
            'count':notification_obj
        }

        async_to_sync(channel_layer.group_send)(
            
            user_id, {
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )
        print("Got to the End!")
