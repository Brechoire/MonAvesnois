"""
Configuration WSGI pour le projet MonAvesnois.

Ce module expose l'application WSGI pour les serveurs web compatibles.
"""

import os
from typing import Any

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application: Any = get_wsgi_application()
