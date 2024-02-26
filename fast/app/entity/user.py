from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    name: str
    email: str
    deleted: bool = False

class UserRequest(BaseModel):
    id: int
    name: str
    email: str
    password: str
