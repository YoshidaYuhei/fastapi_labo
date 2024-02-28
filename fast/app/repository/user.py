import hashlib

from entity.user import UserSignUpIn, UserSignUpInDB
from repository.abstract import BaseRepository
from models.user import User


class UserRepository(BaseRepository):
    def sign_up(self, entity: UserSignUpIn):
        encripted_password = hashlib.sha256(entity.password.encode()).hexdigest()
        in_db = UserSignUpInDB(email=entity.email, encripted_password=encripted_password)
        user = User(**in_db.model_dump())
        self.db.add(user)
        self.db.commit()
        return True

    def is_email_exists(self, email: str) -> bool:
        if self.db.query(User).filter(User.email == email).first():
            return True
        return False