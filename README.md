# QA Python Project

## Description
Ce projet est une API Flask qui implémente un système CRUD pour gérer des utilisateurs. Il inclut des tests unitaires, d'intégration, de performance, ainsi que des tests de sécurité. Le projet utilise une pipeline CI pour automatiser les tests et les analyses de sécurité.

---

## Installation

### Prérequis
- Python 3.x
- Flask
- pytest
- Locust (pour les tests de performance)
- Bandit (pour les tests de sécurité)

### Étapes d'installation

1. Clonez ce dépôt :
```bash
    git clone https://github.com/ton-utilisateur/QA_Python_Project.git
    cd QA_Python_Project
```

2. Créez un environnement virtuel et activez-le :
```bash
    python3 -m venv venv
    source venv/bin/activate  # Pour Linux/Mac
    .\venv\Scripts\activate 
```

3. Installez les dépendances :
```bash
    pip install -r requirements.txt
```

4. Démarrez l'application Flask :
```bash
    python app.py
```

## Utilisation

### Endpoints API

Voici les principaux endpoints de l'API :

- GET /users : Récupère la liste de tous les utilisateurs.
- GET /users/<id> : Récupère un utilisateur spécifique par son ID.
- POST /users : Crée un nouvel utilisateur (données en JSON).
- PUT /users/<id> : Met à jour un utilisateur spécifique.
- DELETE /users/<id> : Supprime un utilisateur spécifique.

### Tests

1. Tests unitaires
Les tests unitaires valident les fonctionnalités isolées de l'API.

Pour exécuter les tests unitaires :
```bash
    pytest tests/unit
```

2. Tests d'intégration
Les tests d'intégration vérifient que les différentes parties du système fonctionnent ensemble correctement.

Pour exécuter les tests d'intégration :
```bash
    pytest tests/integration
```

3. Tests de performance
Les tests de performance sont réalisés avec Locust pour simuler des utilisateurs envoyant des requêtes à l'API.

- Démarrez Locust dans un autre terminal :
```bash
    locust -f locustfile.py --host=http://127.0.0.1:5000
```
- Accédez à l'interface Locust dans votre navigateur : http://localhost:8089
- Configurez le nombre d'utilisateurs à simuler et le taux d'apparition, puis lancez les tests de performance.

4. Tests de sécurité
Les tests de sécurité analysent le code pour détecter des vulnérabilités potentielles.

Pour exécuter les tests de sécurité avec Bandit :
```bash
    bandit -r app.py
```

5. Tests de compatibilité
L'application est testée automatiquement sur plusieurs versions de Python et systèmes d'exploitation via GitHub Actions pour garantir la compatibilité.

- Environnements testés :
    - Versions de Python : 3.9, 3.10
    - Systèmes d'exploitation : Ubuntu, Windows, macOS

6. BDD (Behavior-Driven Development)
Les tests BDD sont écrits avec Behave pour valider les comportements de l'API via des scénarios Gherkin.

Pour exécuter les tests BDD :
```bash
    behave
```

## Intégration continue (CI)
L'intégration continue utilise GitHub Actions. À chaque commit ou pull request, les tests sont exécutés sur plusieurs versions de Python (3.9, 3.10) et systèmes d'exploitation (Ubuntu, Windows, macOS).

Étapes CI :
- Installation des dépendances
- Démarrage du serveur Flask
- Exécution des tests unitaires, d'intégration, et BDD
- Analyse de la couverture du code
- Analyse de sécurité avec Bandit