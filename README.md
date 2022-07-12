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
- `docker build -t DOCKER_ID/oc_lettings:TAG .`

Ajout du docker sur Dockerhub :
- `docker push DOCKER_ID/oc-lettings:TAG`

Lancement du conteneur :
- `run -d -p 8000:8000 DOCKER_ID/oc-lettings:TAG`
- Verification du lancement du conteneur et récupération du CONTAINER_ID `docker ps`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
- arrêt du conteneur `docker stop CONTAINER_ID`


#### Heroku
Ajout d'un compte Heroku : 

- `https://signup.heroku.com/` et créer un compte avec une adresse mail et un password

Installation de heroku CLI : 

https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli


Ajout de l'application sur Heroku :

1- créer l'application [oc-lettings-xx] et lui ajouter 2 variables d'environnement
- SECRET_KEY = [valeur de la secret Key choisie]
- DJANGO_SETTINGS_MODULE = oc_lettings_site.prod_settings

2- pusher le conteneur créer plus haut sur heroku : 
- `heroku login`
- `heroku container:login`
- `heroku container:push -a [oc-lettings-xx] web`
- `heroku container:release -a [oc-lettings-xx] web`
- Verifier le fonctionnement de l'application sur `https://[oc-lettings-xx].herokuapp.com/`

### Configuration de CircleCI
1- Se connecter via github sur la plateforme CircleCI et autoriser l'application circleci : https://circleci.com/signup/

2- Repérer le projet sur Circleci et cliquer sur 'Set Up Project'

- sélectionner `If you already have .circleci/config.yml in your repo, select the branch it's on to start building`
- sélectionner la branche 'master'
- le pipeline va se lancer

3- Configurer les variables d'environnement dans le pipeline
- ajouter dans `Project settings` => `Environment Variables` :
    - Name: DOCKER_PASS, Value: [YOUR_DOCKER_PASSWORD]
    - Name: DOCKER_USER, Value: [YOUR_DOCKER_ID]
    - Name: HEROKU_API_KEY, Value: [YOUR_HEROKU_API_KEY]
    - Name: HEROKU_APP_NAME, Value: [oc-lettings-xx]
    - Name: HEROKU_TOKEN, Value: [YOUR_HEROKU_TOKEN] (pour l'obtenir `heroku authorizations:create`)
    - Name: SENTRY_DSN, Value: SENTRY_DSN

=> A chaque git push de la branche master, l'application est testée, un conteneur est crée avec un tag correspondant au hash du commit
  et stocké sur dockerhub et l'application sur Heroku est mise a jour

## Gestion des erreurs avec Sentry
- `https://sentry.io/signup/` connexion avec github
- Creer un projet avec Django
- Récupérer le dsn ('https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.ingest.sentry.io/xxxxxxx')
- Ajouter le dsn en tant que variable d'environnement dans heroku Name: SENTRY_DSN, Value: [YOUR_DSN]
- Test d'une erreur `https://[oc-lettings-xx].herokuapp.com/sentry-debug/`
- Voir l'erreur `https://sentry.io/organizations/[SENTRY_ID]/issues/`