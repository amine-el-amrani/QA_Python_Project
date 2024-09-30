# QA Python Project

## Description
This project is a Flask API that implements a CRUD system to manage users. It includes unit tests, integration tests, performance tests, security tests, Compatibility tests and BDD tests. The project uses a CI pipeline to automate the tests and security analysis.

---

## Installation

### Prerequisites
- Python 3.x
- Flask
- pytest
- Locust (pour les tests de performance)
- Bandit (pour les tests de sécurité)

### Étapes d'installation

1. Clone this repository: :
```bash
    git clone https://github.com/amine-el-amrani/QA_Python_Project.git
    cd QA_Python_Project
```

2. Create a virtual environment and activate it:
```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    .\venv\Scripts\activate   # For Windows
```

3. Install dependencies:
```bash
    pip install -r requirements.txt
```

4. Start the Flask application:
```bash
    python app.py
```

## Usage

### API Endpoints

Here are the main API endpoints:

- GET /users: Retrieves the list of all users.
- GET /users/<id>: Retrieves a specific user by ID.
- POST /users: Creates a new user (data in JSON).
- PUT /users/<id>: Updates a specific user.
- DELETE /users/<id>: Deletes a specific user.

### Tests

1. Unit tests:
Unit tests validate isolated functionalities of the API.

To run the unit tests:
```bash
    pytest tests/unit
```

2. Integration tests:
Integration tests check that different parts of the system work together correctly.

To run the integration tests:
```bash
    pytest tests/integration
```

3. Performance tests:
Performance tests are done using Locust to simulate users sending requests to the API.

Start Locust in another terminal:
```bash
    locust -f locustfile.py --host=http://127.0.0.1:5000
```
- Access the Locust interface in your browser: http://localhost:8089
- Set the number of users to simulate and the spawn rate, then start the performance tests.

4. Security tests:
Security tests analyze the code to detect potential vulnerabilities.

To run security tests with Bandit:
```bash
    bandit -r app.py
```

5. Compatibility tests:
he application is automatically tested on multiple Python versions and operating systems via GitHub Actions to ensure compatibility.

- Tested environments:
    - Python versions: 3.9, 3.10
    - Operating systems: Ubuntu, Windows, macOS

6. BDD (Behavior-Driven Development):
BDD tests are written with Behave to validate API behaviors via Gherkin scenarios.

To run the BDD tests:
```bash
    behave
```

## Continuous Integration (CI)
The project uses GitHub Actions for continuous integration. On every commit or pull request, tests are run on multiple Python versions (3.9, 3.10) and operating systems (Ubuntu, Windows, macOS).

CI Steps:
- Install dependencies
- Start the Flask server
- Run unit, integration, and BDD tests
- Run code coverage analysis
- Run security analysis with Bandit