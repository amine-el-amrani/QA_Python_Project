import pytest

@pytest.fixture
def client():
    from app import app
    with app.test_client() as client:
        yield client

def test_create_and_get_user(client):
    # Créer un nouvel utilisateur
    response = client.post('/users', json={"name": "Integration Test User"})
    assert response.status_code == 201
    new_user = response.get_json()
    
    # Vérifier que l'utilisateur a été ajouté correctement
    assert new_user['name'] == "Integration Test User"
    
    # Récupérer cet utilisateur par son ID
    response = client.get(f'/users/{new_user["id"]}')
    assert response.status_code == 200
    assert response.get_json()['name'] == "Integration Test User"

def test_update_user(client):
    # Créer un utilisateur pour le mettre à jour ensuite
    response = client.post('/users', json={"name": "User to Update"})
    assert response.status_code == 201
    user_to_update = response.get_json()
    
    # Mettre à jour le nom de cet utilisateur
    response = client.put(f'/users/{user_to_update["id"]}', json={"name": "Updated User"})
    assert response.status_code == 200
    
    # Vérifier que le nom a été mis à jour
    updated_user = response.get_json()
    assert updated_user['name'] == "Updated User"

def test_delete_user(client):
    # Créer un utilisateur pour le supprimer ensuite
    response = client.post('/users', json={"name": "User to Delete"})
    assert response.status_code == 201
    user_to_delete = response.get_json()
    
    # Supprimer cet utilisateur
    response = client.delete(f'/users/{user_to_delete["id"]}')
    assert response.status_code == 200
    assert response.get_json()['message'] == "User deleted"
    
    # Vérifier que l'utilisateur n'existe plus
    response = client.get(f'/users/{user_to_delete["id"]}')
    assert response.status_code == 404