# chat/routing.py
from django.urls import re_path
from django.conf.urls import url
from . import consumers

# TheSocialClub

websocket_urlpatterns = [
    url(r"^TheSocialClub/posts/in_friend/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$", consumers.EchoConsumer.as_asgi())
]