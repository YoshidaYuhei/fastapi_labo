from typing import Optional

from fastapi import Depends
# from depends.di_container import user_repository
from sqlalchemy.orm import Session
from pydantic import validator
from entity.abstract import BaseEntity

class BaseUser(BaseEntity):
    name: str
    email: str
    deleted: bool = False

class UserSignUpIn(BaseEntity):
    email: str
    password: str
    
    # @validator('email')
    # def email_exists(cls, v, user_repo=Depends(user_repository)):
    #     return user_repo.is_email_exists(v)

class UserLoginIn(BaseEntity):
    email: str
    password: str

class UserSignUpInDB(BaseEntity):
    email: str
    encripted_password: str
