from fastapi import Depends
from sqlalchemy.orm import Session
from depends.get_db import get_db

class BaseRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db