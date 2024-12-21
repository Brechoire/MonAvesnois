# 🌳 Mon Avesnois

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)](https://www.djangoproject.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Django CI](https://github.com/Brechoire/MonAvesnois/actions/workflows/django.yml/badge.svg)](https://github.com/Brechoire/MonAvesnois/actions/workflows/django.yml)
[![codecov](https://codecov.io/gh/Brechoire/MonAvesnois/branch/main/graph/badge.svg)](https://codecov.io/gh/Brechoire/MonAvesnois)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

> 🌿 Découvrez les professionnels qui font vivre l'Avesnois.

## 📖 À propos

Mon Avesnois est une plateforme web dédiée à la mise en valeur des TPE, PME, Associations et Entreprises de l'Avesnois. Ce projet utilise Django pour offrir une expérience utilisateur moderne et responsive.

## ✨ Fonctionnalités

- 🏠 Page d'accueil moderne et responsive
- 🎨 Design élégant avec Bootstrap
- 🔍 Navigation intuitive
- 📱 Compatible mobile

## 🛠️ Technologies

- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=Python&logoColor=white) Python 3.12
- ![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=Django&logoColor=white) Django 5.1.4
- ![Bootstrap](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat&logo=Bootstrap&logoColor=white) Bootstrap 5
- ![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=SQLite&logoColor=white) SQLite (dev)

## 🚀 Installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/brechoire/MonAvesnois.git
cd MonAvesnois
```

2. **Créer un environnement virtuel**
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\\Scripts\\activate   # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Pour le développement
```

4. **Configurer l'environnement**
```bash
# Créer un fichier .env à la racine du projet
cp .env.example .env
# Modifier les variables dans .env
```

5. **Appliquer les migrations**
```bash
python manage.py migrate
```

6. **Lancer le serveur**
```bash
python manage.py runserver
```

## 🧪 Tests

Le projet utilise le framework de test intégré de Django. Pour exécuter les tests :

```bash
python manage.py test
```

## 📝 Qualité du Code

Le projet utilise plusieurs outils pour maintenir une qualité de code élevée :

- **Black** : Formatage du code
- **isort** : Tri des imports
- **flake8** : Style et qualité
- **pylint** : Analyse statique
- **mypy** : Vérification des types

Pour exécuter les vérifications :

```bash
pre-commit run --all-files
```

## 🔧 Configuration

Le projet utilise des variables d'environnement pour la configuration. Créez un fichier `.env` avec :

```env
SECRET_KEY=votre-clé-secrète
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 📦 Structure du Projet

```
MonAvesnois/
├── app/                    # Configuration principale
├── main/                   # Application principale
├── static/                 # Fichiers statiques
├── templates/              # Templates globaux
├── manage.py              # Script Django
├── requirements.txt       # Dépendances
└── requirements-dev.txt   # Dépendances de développement
```

## 🚀 Déploiement

1. **Préparer l'environnement de production**
```bash
DEBUG=False
ALLOWED_HOSTS=votre-domaine.com
```

2. **Collecter les fichiers statiques**
```bash
python manage.py collectstatic
```

3. **Configurer le serveur web (exemple avec Nginx)**
```nginx
server {
    listen 80;
    server_name votre-domaine.com;
    location /static/ {
        alias /chemin/vers/staticfiles/;
    }
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## 👥 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Contact

brechoire.j@gmail.com

Lien du projet : [https://github.com/brechoire/MonAvesnois](https://github.com/brechoire/MonAvesnois)

---

<p align="center">
  Fait avec ❤️ pour l'Avesnois
</p>
