# CalculettePolonaiseNPI

## Première info documentation API

- Pour avoir plus d'info sur les routes API aller sur cette url ```http://localhost:8000/docs#/ ``` une fois le back lancer

- Il y a deux routes :
    - Une qui permet de retourner le calcul
    - La deuxième qui permet de renvoyer un fichier CSV des calculs

## Docker

- Il y a 2 fichiers dockerfile et un docker compose
    - Le premier Dockerfile est la mise en place du backend
    - Le deuxième la mise en place du frontend
    - Le docker compose à 3 partie un container front back et un container pour la base de données

- Différente commande pour lancer les container et docker
    - ``` docker-compose up --build``` permet pour la première fois de build et de lancer les containers
    - ``` docker-compose down``` permet de stopper et supprimer les container

## Frontend

- Pour le frontend le lien pour y accéder est ```http://localhost:3000/ ```
- Pour lancer le front en local sans docker ```npm start ```
- Le front est en react tout le code est dans l'app.js et le style dans l'index.css

## Backend

- Pour le backend le lien ```http://localhost:8000/ ```
- Pour lancer le back en local sans docker ```cd backend/app ```
```py -m run uvicorn main:app --host 0.0.0.0 --port 8000 --reload ```

## Pour les test

- Commande pour vérifier les test ``` cd backend/test ``` ensuite ``` py -m pytest```