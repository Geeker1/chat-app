from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.routing import ProtocolTypeRouter

from chat.consumers import ChatConsumer
application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter(
				[
					url(r"^messages/(?P<username>[\w.@+-]+)", ChatConsumer),
				]
				))
		)
	})



#ws://ourdomain/<username>







"""Allowed HostsOriginValidator ensures that the host or dommain name doing the websocket a
matches the one declared in the settings of the project

AuthiddleWareStack If You want the requesting user to be inside the websocket
, it is siilar to middleware for the routing and it justs adds the security check, and
it allos to get the user been requested
"""