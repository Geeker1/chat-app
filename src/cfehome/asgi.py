"""This file is needed when you go into production so u dont use the wsgi but the asgi"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cfehome.settings")
django.setup()
application = get_default_application()