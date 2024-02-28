from fastapi import Depends
from faker import Faker
from sqlalchemy.orm import Session
from entity.user import UserSignUpIn
from models.user import User
from repository.user import UserRepository


def test_sign_up(db: Session, fake: Faker):
    # input
    test_user_request = UserSignUpIn(email=fake.email(), password=fake.password())

    # exec
    user_repo = UserRepository(db=db)
    result = user_repo.sign_up(test_user_request)

    # 返り値が true であること
    assert result is True

    # DBに登録されていること
    user_in_db = db.query(User).filter(User.email == test_user_request.email).first()
    assert user_in_db is not None
    assert user_in_db.email == test_user_request.email

def test_is_email_exists(db: Session, fake: Faker):
    # input
    email = fake.email()
    user = User(email=email)
    db.add(user)
    db.commit()
    
    # exec
    user_repo = UserRepository(db=db)
    result = user_repo.is_email_exists(email)
    
    # Trueを返すこと
    assert result is True
    