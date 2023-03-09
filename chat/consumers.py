import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        recipient = self.scope["url_route"]["kwargs"]["room_name"]
        sender = self.scope["user"].username

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        self.room_id = await self.get_room_id(sender, recipient)
        self.room_group_name = f'{self.room_id}' # "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(
                self.room_group_name, self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message", 
                "message": message,
                "recipient": self.room_name,
                "sender": self.scope["user"].username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": event["sender"],
            "recipient": event["recipient"],
        }))

    @database_sync_to_async
    def get_room_id(self, username1, username2):
        return Room.get_or_create(username1, username2)

    @database_sync_to_async
    def store_message(self, sender, recipient, message):
        return Message.objects.create(sender=sender, recipient=recipient, message=message)
