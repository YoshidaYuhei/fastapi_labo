from fastapi import APIRouter, Depends
from depends.di_container import user_repository
from entity.user import UserSignUpIn
from repository.user import UserRepository

router = APIRouter()

@router.post("/signup", response_model=None)
async def signup(request: UserSignUpIn, user_repo: UserRepository = Depends(user_repository)):
    user_repo.sign_up(request)
    return True
