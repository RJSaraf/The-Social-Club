"""
ASGI config for Quantum_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import TheSocialClub.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Quantum_django.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AllowedHostsOriginValidator( 
    AuthMiddlewareStack(
        URLRouter(
            TheSocialClub.routing.websocket_urlpatterns
        )
    )
  )
})





