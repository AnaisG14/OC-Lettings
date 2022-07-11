## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/AnaisG14/OC-Lettings.git

#### Créer l'environnement virtuel

- `cd /path/to/OC-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/OC-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/OC-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/OC-Lettings`
- `source venv/bin/activate`
- `pytest`

#### Base de données (accès et consultation)

- `cd /path/to/OC-Lettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Lancer le serveur via `python manage.py runserver`
- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Intégration continue et déploiement continu via un pipeline Circleci

### Prérequis
#### Docker (installation et utilisation)

Installation de Docker
- Installer Docker pour Ubuntu: https://docs.docker.com/desktop/linux/install/ubuntu/
- Installer Docker pour Windows : https://docs.docker.com/desktop/windows/install/
- Installer Docker pour Mac : https://docs.docker.com/desktop/mac/install/

Ajout d'un compte sur Dockerhub :
- `https://hub.docker.com/ avec la création d'un DOCKER_ID et un DOCKER_PASSWORD`
- `docker login (avec DOCKER_ID et DOCKER_PASSWORD)`

Création d'un conteneur :
- `cd /path/to/OC-Lettings`
- `docker build -t oc-lettings .`
- `docker tag oc-lettings oc-lettings:latest`

Ajout du docker sur Dockerhub :
- `docker push DOCKER_ID/oc-lettings:latest`

Lancement du conteneur :
- `run -d -p 8000:8000 oc-lettings`
- Verification du lancement du conteneur et récupération du CONTAINER_ID `docker ps`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
- arrêt du conteneur `docker stop CONTAINER_ID`


#### Heroku
Ajout d'un compte Heroku : 

- `https://signup.heroku.com/` avec une adresse mail et un password

Installation de heroku CLI : 

https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli


Ajout de l'application sur Heroku :

1- créer l'application et lui ajouter 2 variables d'environnement
- SECRET_KEY = [valeur de la secret Key]
- DJANGO_SETTINGS_MODULE = oc_lettings_site.prod_settings

2- relier l'application heroku avec le repository git : 
- `heroku login` (connexion avec le navigateur web)
- `heroku container:login`
- `heroku container:push -a [nom_app] web`
- {heroku container:release -a [nom_app] web}
- Verifier le fonctionnement de l'application sur `https://o[nom_app].herokuapp.com/`


## Gestion des erreurs avec Sentry
