"""Vues de l'application principale.

Ce module définit les vues pour l'application principale
de MonAvesnois. Il gère le rendu des templates et la logique
métier associée à chaque vue.
"""

from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_view(request: HttpRequest) -> HttpResponse:
    """
    Vue de la page d'accueil.

    Args:
        request: La requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP avec le template rendu.
    """
    context: dict[str, Any] = {
        "title": "Accueil",
    }
    return render(request, "main/home.html", context)
