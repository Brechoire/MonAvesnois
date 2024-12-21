"""Configuration des URLs de l'application principale.

Ce module définit les URLs spécifiques à l'application principale,
notamment la page d'accueil et les autres vues du site.
"""

from django.urls import URLPattern, path

from . import views

app_name: str = "main"

urlpatterns: list[URLPattern] = [
    path("", views.home_view, name="home"),
]
