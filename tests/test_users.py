from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_create_user():
    new_user = {
        "email": "teste@email.com",
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "password": "123456",
        "role": "user"
    }
    response = client.post("/auth/", json=new_user)
    assert response.status_code == 201
    assert response.json()["email"] == new_user["email"]