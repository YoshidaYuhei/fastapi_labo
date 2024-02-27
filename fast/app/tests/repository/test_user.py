from sqlalchemy.orm import Session
from entity.user import UserCreateIn
from models import User
from repository.user import create


def test_create_user(db: Session):
    # テスト用のUserRequestを作成します
    test_user_request = UserCreateIn(name="test", email="test@example.com")

    # メソッドを呼び出します
    result = create(test_user_request, db)

    assert result is True

    # データベースにユーザーが正しく保存されていることを確認します
    user_in_db = db.query(User).filter(User.email == test_user_request.email).first()
    assert user_in_db is not None
    assert user_in_db.name == test_user_request.name
    assert user_in_db.email == test_user_request.email