from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Body, Depends
from fastapi import Response
from fastapi import status

from lib.auth.jwt_token import create_access_token, create_refresh_token

router = APIRouter()

@router.post("/token")
async def generate_token(email: Annotated[str, Body(...)]):
    return {"access_token": create_access_token(email), "refresh_token": create_refresh_token(email), "token_type": "bearer"}
