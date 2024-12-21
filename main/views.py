"""Vues de l'application principale.

Ce module définit les vues pour l'application principale
de MonAvesnois. Il gère le rendu des templates et la logique
métier associée à chaque vue.
"""

from typing import Any, Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Affiche la page d'accueil.

    Args:
        request: La requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP contenant la page d'accueil.
    """
    context: Dict[str, Any] = {
        "title": "Accueil",
        "description": "Bienvenue sur Mon Avesnois",
    }
    return render(request, "main/home.html", context)
