from faker import Faker
from sqlalchemy.orm import Session
from entity.user import UserCreateIn
from models import User
from repository.user import create


def test_create_user(db: Session, fake: Faker):
    # 入力
    test_user_request = UserCreateIn(name=fake.name(), email=fake.email())

    # 実行
    result = create(test_user_request, db)

    # 返り値が true であること
    assert result is True

    # DBに登録されていること
    user_in_db = db.query(User).filter(User.email == test_user_request.email).first()
    assert user_in_db is not None
    assert user_in_db.name == test_user_request.name
    assert user_in_db.email == test_user_request.email