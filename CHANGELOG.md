# 📋 Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2024-12-21

### 🔧 Corrigé
- ✍️ Ajout des annotations de type pour les URLs Django
- 🔄 Correction des types URLPattern et URLResolver
- 🏷️ Ajout du namespace pour l'application principale
- 🐛 Correction du nom de la vue home_view

## [1.2.0] - 2024-12-21

### 🔄 Changé
- ⚡️ Simplification du workflow CI en supprimant Codecov
- 📊 Intégration de la couverture de tests directement dans le job principal
- 📈 Génération de rapports de couverture HTML
- 🔍 Upload des rapports comme artifacts GitHub
- 🧹 Nettoyage des badges dans le README

### 🗑️ Supprimé
- 🔌 Dépendance à Codecov
- 🏷️ Badge Codecov du README

## [1.1.3] - 2024-12-21

### 🔧 Modifié
- 🔑 Ajout du support du token Codecov dans le workflow CI
- 📝 Activation du mode verbose pour Codecov
- 🔍 Amélioration du débogage des erreurs de couverture

## [1.1.2] - 2024-12-21

### 🐛 Corrigé
- 🔐 Configuration correcte des variables d'environnement dans GitHub Actions
- 📁 Création automatique du dossier static dans l'environnement CI
- 🔧 Amélioration de la configuration des jobs de test et coverage

## [1.1.1] - 2024-12-21

### 🔧 Modifié
- ⚙️ Suppression de safety des dépendances pour résoudre un conflit avec black
- 🔄 Simplification du workflow CI pour n'utiliser que bandit pour la sécurité
- 📦 Mise à jour des dépendances de développement

## [1.1.0] - 2024-12-21

### ✨ Ajouté
- 🔄 Configuration GitHub Actions pour CI/CD
- 🧪 Tests automatisés avec Django CI
- 📊 Intégration de la couverture de code avec Codecov
- 🔒 Analyse de sécurité avec Bandit
- 📝 Nouveaux badges dans le README
- 📦 Dépendances de développement pour tests et sécurité

## [1.0.1] - 2024-12-21

### 🐛 Corrigé
- ✍️ Ajout des annotations de type manquantes dans les tests
- 📝 Simplification des docstrings des tests
- 🔍 Correction du formatage des imports

## [1.0.0] - 2024-12-21

### ✨ Ajouté
- 🎨 Mise en place de la structure initiale du projet Django
- 🏠 Création de la page d'accueil responsive
- 🔒 Configuration de la sécurité avec variables d'environnement
- 📱 Support mobile avec Bootstrap 5
- 🧪 Tests unitaires de base

### 🛠️ Configuration
- ⚙️ Configuration de pre-commit avec:
  - Black pour le formatage
  - isort pour le tri des imports
  - flake8 pour le style
  - pylint pour la qualité
  - mypy pour le typage
- 📦 Mise en place des requirements.txt et requirements-dev.txt
- 🗃️ Configuration de la base de données SQLite

### 📚 Documentation
- 📖 Création du README.md détaillé
- 📝 Documentation du code avec docstrings
- 📋 Ajout du CHANGELOG.md

## [0.2.0] - 2024-12-21

### ✨ Ajouté
- 🎨 Configuration initiale de Django
- 📱 Intégration de Bootstrap
- 🗃️ Configuration de la base de données

### 🛠️ Configuration
- ⚙️ Configuration de base de Django
- 📦 Installation des dépendances principales

## [0.1.0] - 2024-12-21

### ✨ Ajouté
- 🎉 Initialisation du projet
- 📁 Création de la structure des dossiers
- 📝 Configuration Git

[1.2.1]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.2.1
[1.2.0]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.2.0
[1.1.3]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.1.3
[1.1.2]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.1.2
[1.1.1]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.1.1
[1.1.0]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.1.0
[1.0.1]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.0.1
[1.0.0]: https://github.com/Brechoire/MonAvesnois/releases/tag/v1.0.0
[0.2.0]: https://github.com/Brechoire/MonAvesnois/releases/tag/v0.2.0
[0.1.0]: https://github.com/Brechoire/MonAvesnois/releases/tag/v0.1.0
