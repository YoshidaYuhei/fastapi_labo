from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Body, Depends
from fastapi import Response
from fastapi import status

from lib.auth.jwt_token import create_access_token, create_refresh_token
from entity.user import UserSignUpIn
from repository.user import UserRepository
from depends.di_container import user_repository

router = APIRouter()

@router.post("/signup", response_model=None)
async def signup(request: UserSignUpIn, user_repo: UserRepository = Depends(user_repository)):
    user_repo.sign_up(request)
    return True

@router.post("/login")
async def generate_token(email: Annotated[str, Body(...)]):
    return {"access_token": create_access_token(email), "refresh_token": create_refresh_token(email), "token_type": "bearer"}
