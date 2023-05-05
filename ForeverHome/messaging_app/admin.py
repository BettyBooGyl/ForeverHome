from django.contrib import admin
from messaging_app.models import Message, Notification
admin.site.register(Message)
admin.site.register(Notification)