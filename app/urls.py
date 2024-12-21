"""Configuration des URLs du projet MonAvesnois.

Ce module définit les URLs principales du projet et inclut
les URLs des applications. Il gère également la configuration
des fichiers statiques et média en mode développement.
"""

from typing import List, Union

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Configuration des URLs principales
urlpatterns: List[Union[path, static]] = [
    # Interface d'administration Django
    path("admin/", admin.site.urls),
    # URLs de l'application principale
    path("", include("main.urls")),
]

# Configuration des fichiers statiques et média en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
