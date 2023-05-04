import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from messaging_app.models import Message
from profile_app.models import Profile


class ChatConsumer(AsyncWebsocketConsumer):
    # async def connect(self):
    #     my_id = self.scope['user'].id
    #     other_user_id = self.scope['url_route']['kwargs']['id']
    #     if int(my_id) > int(other_user_id):
    #         self.room_name = f'{my_id}-{other_user_id}'
    #     else:
    #         self.room_name = f'{other_user_id}-{my_id}'

    #     self.room_group_name = 'chat_%s' % self.room_name

    #     await self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )
    async def connect(self):
            print(self.scope['url_route']['kwargs']['id1'] + self.scope['url_route']['kwargs']['id2'])
            self.room_name = self.scope['url_route']['kwargs']['id1']  + self.scope['url_route']['kwargs']['id2'] 
            
            print(self.room_name)
            self.room_group_name = "chat_%s" % self.room_name
            print(self.room_group_name)

            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)

            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json['username']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'username':username}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Send message to WebSocket
        await self.save_message(username, self.room_group_name, message)
        await self.send(text_data=json.dumps({"message": message, 'username':username}))
    
    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        message_object = Message.objects.create(sender = Profile.objects.get(username=username), message=message, thread_name = thread_name) 