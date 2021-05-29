import asyncio
import json
from asgiref.sync import async_to_sync , sync_to_async
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer

# TheSocialClub
from TheSocialClub.models import Group, GroupMember, Post, FriendsList, PrivateMessage
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
User = get_user_model()

class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
            "type": "websocket.accept",
        })

        #await asyncio.sleep(10)
       

    async def websocket_receive(self, event):
        print('recieve', event)
        front_text = event.get('text', None)
        if front_text is not None:
           loaded_dict_data = json.loads(front_text)
           msg = loaded_dict_data.get('message')
        
        await self.msgsave(message=msg)

        await self.send({
            'type': 'websocket.send',
            'text': msg
        })

    async def websocket_disconnect(self, event):
        print('disconnected', event)

'''
    @database_sync_to_async
    def msgsave(self, message, *args, **kwargs):
        sender = get_object_or_404(User, username=self.scope['user'])
        reciever = get_object_or_404(User, username=self.scope['url_route']['kwargs']['slug'])
        privatemsg = PrivateMessage.objects.create(sender=sender, reciever=reciever, msg_content=message)
        privatemsg.save()

'''