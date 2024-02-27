from entity.abstract import BaseEntity

class BaseUser(BaseEntity):
    name: str
    email: str
    deleted: bool = False

class UserCreateIn(BaseUser):
    pass