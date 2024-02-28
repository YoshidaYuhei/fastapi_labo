from faker import Faker
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from models.user import User

def test_sign_up(db: Session, client: TestClient, fake: Faker):
    # 入力
    request = {"email": fake.name(), "password": fake.password()}

    # 実行
    response = client.post("/user/signup", json=request)
    assert response.status_code == 200

    # DBに登録されていること
    user_in_db = db.query(User).filter(User.email == request["email"]).first()
    assert user_in_db is not None
