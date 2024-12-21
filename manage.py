#!/usr/bin/env python
"""Script de gestion Django.

Ce script est l'utilitaire en ligne de commande de Django pour les
tâches administratives.
"""

import os
import sys
from typing import NoReturn


def main() -> NoReturn:
    """Point d'entrée principal du script.

    Configure l'environnement Django et exécute les commandes
    administratives.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Êtes-vous sûr qu'il est "
            "installé et disponible dans votre PYTHONPATH ? Avez-vous "
            "oublié d'activer un environnement virtuel ?"
        ) from exc
    execute_from_command_line(sys.argv)
    sys.exit(0)


if __name__ == "__main__":
    main()
