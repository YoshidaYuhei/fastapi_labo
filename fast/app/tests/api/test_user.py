from faker import Faker
from fastapi.testclient import TestClient


def test_create_user(client: TestClient, fake: Faker):
    # 入力
    request = {"name": fake.name(), "email": fake.email()}

    # 実行
    response = client.post("/user", json=request)
    assert response.status_code == 200