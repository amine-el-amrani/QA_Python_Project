import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.get_json()) >= 0

def test_get_single_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json()['id'] == 1

def test_create_user(client):
    response = client.post('/users', json={"name": "Test User"})
    assert response.status_code == 201
    assert response.get_json()['name'] == "Test User"

def test_update_user(client):
    response = client.put('/users/1', json={"name": "Updated User"})
    assert response.status_code == 200
    assert response.get_json()['name'] == "Updated User"

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.get_json()['message'] == "User deleted"