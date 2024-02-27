from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
from depends import get_db
from sqlalchemy.orm import Session
from entity import UserCreateIn
from repository import create as repo_create

router = APIRouter()

@router.post("/", response_model=None)
async def create(request: UserCreateIn, db: Annotated[Session, Depends(get_db)]):
    repo_create(request, db)
    return True
