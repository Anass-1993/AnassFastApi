
# FastAPI ANASS

## Présentation
Ce projet est une API REST développée avec **FastAPI** permettant la gestion d’objets (items) avec des opérations CRUD (Create, Read, Update, Delete).  
L’API est testée automatiquement, analysée par un linter (flake8) et déployée en continu sur [Render](https://render.com) via GitHub Actions.

## Fonctionnalités

- Création, lecture, modification et suppression d’items
- Documentation interactive automatique via Swagger UI (`/docs`)
- Pipeline CI/CD (lint + tests) avec GitHub Actions
- Déploiement automatique sur Render à chaque push sur la branche principale

---

## Installation locale

### 1. Cloner le dépôt
```
https://github.com/Anass-1993/AnassFastApi.git
```

### 2. Créer un environnement virtuel


```
python -m venv venv
source venv/bin/activate # ou venv\Scripts\activate sous Windows
```

### 3. Installer les dépendances

```
pip install -r requirements.txt
```

## Lancer l’API en local

```
uvicorn main:app --reload
```

L’API sera accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

- Documentation Swagger : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Documentation Redoc : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Linting du code

Pour vérifier la qualité du code avec flake8 :


---

## Lancer les tests unitaires


---

## CI/CD avec GitHub Actions

À chaque push ou pull request sur la branche principale :

- Le linter flake8 vérifie la qualité du code
- Les tests unitaires sont exécutés avec pytest
- Si tout est OK, Render déploie automatiquement la nouvelle version

---

## Déploiement automatique sur Render

- L’application est déployée sur [Render](https://render.com).
- À chaque mise à jour du code sur la branche principale, Render effectue :
  - Installation des dépendances
  - Lancement de l’application avec :  
    ```
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```
- L’URL publique de l’API est :  
```
https://<ton-service>.onrender.com
```
(Remplace `<ton-service>` par le nom de ton service Render)

---

## Structure du projet

```
├── main.py
├── models.py
├── requirements.txt
├── tests/
│ ├── init.py
│ └── test_items.py
├── .github/
│ └── workflows/
│ └── ci.yml
├── README.md
```

---

## Exemples d’utilisation

### Récupérer tous les items

```
GET /items
```

### Créer un nouvel item

```
POST /items
Content-Type: application/json

{
"id": 1,
"name": "Livre",
"price": 10.0,
"in_stock": true
}
```

---

## Captures d’écran

- **Pipeline GitHub Actions réussi**  
  *(Insère ici une capture d’écran de l’action GitHub réussie)*

- **API en ligne sur Render**  
  *(Insère ici une capture d’écran de l’API sur Render)*

---

## Auteur

- Anass ER-RIYACHY

