import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from messaging_app.models import Message, Notification
from profile_app.models import Profile

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].userID
        self.room_group_name = f'{my_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        count = data['count']
        print(count)
        await self.send(text_data=json.dumps({
            'count':count
        }))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
            print(self.scope['url_route']['kwargs']['id1'] + self.scope['url_route']['kwargs']['id2'])
            self.room_name = self.scope['url_route']['kwargs']['id1']  + self.scope['url_route']['kwargs']['id2'] 
            
            print(self.room_name)
            self.room_group_name = "chat_%s" % self.room_name
            print(self.room_group_name)

            await self.channel_layer.group_add(self.room_group_name, self.channel_name)

            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']
        await self.save_message(username, self.room_group_name, message, receiver)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Send message to WebSocket
        
        await self.send(text_data=json.dumps({"message": message, 'username':username}))
    
    @database_sync_to_async
    def save_message(self, username, thread_name, message, reciver):
        message_object = Message.objects.create(sender = Profile.objects.get(username=username), message=message, thread_name = thread_name) 
        print(self.scope['url_route']['kwargs']['id1'])
        print(self.scope['user'].userID)
        print(Profile.objects.get(userID=self.scope['url_route']['kwargs']['id1']) == self.scope['user'])
        if (Profile.objects.get(userID=self.scope['url_route']['kwargs']['id1']) == self.scope['user']):
            other_user_id = self.scope['url_route']['kwargs']['id2']
        else:
            other_user_id = self.scope['url_route']['kwargs']['id1']

        print(other_user_id)
        print(reciver)
        
        get_user = Profile.objects.get(userID=other_user_id)
        print(get_user)
        if (reciver == get_user.username):
            print(get_user)
            notification_obj = Notification.objects.create(message = message_object, user=get_user)
            print("CREATED")