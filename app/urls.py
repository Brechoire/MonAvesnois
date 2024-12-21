"""URL configuration for app project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path

urlpatterns: list[URLPattern | URLResolver] = [
    # Interface d'administration Django
    path("admin/", admin.site.urls),
    # URLs de l'application principale
    path("", include("main.urls", namespace="main")),
]

# Configuration des fichiers statiques et média en mode développement
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
