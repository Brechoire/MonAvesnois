"""Configuration de l'application principale.

Ce module définit la configuration de l'application principale
de MonAvesnois.
"""

from django.apps import AppConfig


class MainConfig(AppConfig):
    """Configuration de l'application principale."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
