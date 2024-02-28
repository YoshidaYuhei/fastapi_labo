from sqlalchemy.orm import Session
from fastapi import Depends
from depends.get_db import get_db

from repository.user import UserRepository

def user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)