"""Configuration des URLs de l'application principale.

Ce module définit les URLs spécifiques à l'application principale,
notamment la page d'accueil et les autres vues du site.
"""

from typing import List, Union

from django.urls import path

from . import views

app_name: str = "main"

urlpatterns: List[Union[path, str]] = [
    path("", views.home, name="home"),
]
