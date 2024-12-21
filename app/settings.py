"""Configuration Django pour le projet MonAvesnois.

Ce module contient les paramètres de configuration Django pour
l'application MonAvesnois. Il inclut tous les paramètres nécessaires
pour le développement et la production, notamment :
    - Sécurité et clés secrètes
    - Configuration des applications et middlewares
    - Paramètres de base de données
    - Internationalisation
    - Gestion des fichiers statiques et média
    - Validation des mots de passe

Les valeurs sensibles sont chargées depuis des variables
d'environnement via le fichier .env pour plus de sécurité.
"""

import os
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Construction des chemins dans le projet
BASE_DIR: Path = Path(__file__).resolve().parent.parent

# Paramètres de sécurité
SECRET_KEY: str = os.getenv("SECRET_KEY", "")
DEBUG: bool = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS: List[str] = os.getenv("ALLOWED_HOSTS", "").split(",")

# Configuration des applications
INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",
]

# Configuration des middlewares
MIDDLEWARE: List[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "app.urls"

TEMPLATES: List[Dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "app.wsgi.application"

# Configuration de la base de données
DATABASES: Dict[str, Dict[str, Any]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Validation des mots de passe
AUTH_PWD_VALIDATION_PATH: str = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
    {
        "NAME": f"{AUTH_PWD_VALIDATION_PATH}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{AUTH_PWD_VALIDATION_PATH}.MinimumLengthValidator",
    },
    {
        "NAME": f"{AUTH_PWD_VALIDATION_PATH}.CommonPasswordValidator",
    },
    {
        "NAME": f"{AUTH_PWD_VALIDATION_PATH}.NumericPasswordValidator",
    },
]

# Configuration de l'internationalisation
LANGUAGE_CODE: str = "fr-fr"
TIME_ZONE: str = "Europe/Paris"
USE_I18N: bool = True
USE_TZ: bool = True

# Configuration des fichiers statiques
STATIC_URL: str = "static/"
STATIC_ROOT: Path = BASE_DIR / "staticfiles"
STATICFILES_DIRS: List[Path] = [BASE_DIR / "static"]

# Configuration des fichiers média
MEDIA_URL: str = "media/"
MEDIA_ROOT: Path = BASE_DIR / "media"

# Type de clé primaire par défaut
DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
