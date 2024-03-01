from faker import Faker
from fastapi import Body
from fastapi.testclient import TestClient

def test_generate_token(client: TestClient, fake: Faker):
    response = client.post("/auth/token", json=fake.email())
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

