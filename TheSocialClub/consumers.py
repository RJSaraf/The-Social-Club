import asyncio
import json
from asgiref.sync import async_to_sync , sync_to_async
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from django.contrib.auth.models import User, auth

# TheSocialClub
from TheSocialClub.models import Group, GroupMember, Post, FriendsList, PrivateMessage
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
            "type": "websocket.accept",
        })   

    async def websocket_receive(self, event):
        print('recieve', event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')

            user = await self.get(msg=msg)
            print(user)
            username=user.username
            email=user.email
            data = {'username':username,
                    'email':email,
                    'message':msg
                    }     

        await self.send({
                'type': 'websocket.send',
                'text': json.dumps(data),
            })

    async def websocket_disconnect(self, event):
        print('disconnected', event)
        
          
    @database_sync_to_async
    def get(self, msg):
        try:
            user = get_object_or_404(User, username=msg)
            return user 
        except Exception:
            print('no user found')        
             
        
        
        #sender = get_object_or_404(User, username=self.scope['user'])
        #reciever = get_object_or_404(User, username=self.scope['url_route']['kwargs']['slug'])
        #privatemsg = PrivateMessage.objects.create(sender=sender, reciever=reciever, msg_content=message)
        #privatemsg.save()





class FriendConsumer(AsyncConsumer):

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
        
        await self.send({
            'type': 'websocket.send',
            'text': msg
        })

    async def websocket_disconnect(self, event):
        print('disconnected', event)