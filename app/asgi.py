"""
Configuration ASGI pour le projet MonAvesnois.

Ce module expose l'application ASGI pour les serveurs web compatibles.
"""

import os
from typing import Any

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application: Any = get_asgi_application()
