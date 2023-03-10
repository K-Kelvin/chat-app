import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.recipient = self.scope["url_route"]["kwargs"]["room_name"]
        self.sender = self.scope["user"].username

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        self.room_id = await self.get_room_id(self.sender, self.recipient)
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

        # save the message to the database
        msg = await self.store_message(
            sender=self.sender,
            recipient=self.recipient,
            message=message
        )
        print(msg)
        print(msg.date)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message", 
                "message": message,
                "recipient": self.recipient,
                "sender": self.sender,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        recipient = event["recipient"]

        # Send message to WebSocket
        if sender != self.sender: # don't re-broadcast the message back to the sender
            await self.send(text_data=json.dumps({
                "message": message,
                "sender": event["sender"],
                "recipient": recipient,
            }))

    @database_sync_to_async
    def get_room_id(self, username1, username2):
        room_id = Room.get_or_create(username1, username2)
        return room_id

    @database_sync_to_async
    def store_message(self, sender, recipient, message):
        return Message.add_new(sender_uname=sender, recipient_uname=recipient, message=message)
