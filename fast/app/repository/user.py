
from entity.user import UserCreateIn
from sqlalchemy.orm import Session
from models import User as UserModel


def create(entity: UserCreateIn, db: Session):
    user = UserModel(**entity.model_dump())
    db.add(user)
    db.commit()
    return True