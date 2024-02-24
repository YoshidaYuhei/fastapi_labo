from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    id: int
    name: str
    email: str
    password: str