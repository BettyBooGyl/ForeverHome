from django.urls import re_path, path


from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<id1>\w+)(?P<id2>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/notify/$", consumers.NotificationConsumer.as_asgi())
]