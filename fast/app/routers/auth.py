from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Body, Depends
from fastapi import Response
from fastapi import status

from lib.auth.jwt_token import create_access_token, create_refresh_token
from entity.user import UserLoginIn, UserSignUpIn
from repository.user import UserRepository
from depends.di_container import user_repository

router = APIRouter()

@router.post("/signup", response_model=None)
async def signup(request: UserSignUpIn, user_repo: UserRepository = Depends(user_repository)):
    user_repo.sign_up(request)
    return True

@router.post("/login")
async def generate_token(request: UserLoginIn, user_repo: UserRepository = Depends(user_repository)):
    if user_repo.validate_password(request.email, request.password):
        return {"access_token": create_access_token(request.email), "refresh_token": create_refresh_token(request.email), "token_type": "bearer"}
    else:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
