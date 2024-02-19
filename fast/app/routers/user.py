from fastapi import APIRouter
from fastapi import Response
from fastapi import status

from entity import UserIn
from entity import UserOut

router = APIRouter()


@router.get("/user/profile", response_model=UserOut)
async def get_profile(email: str, password: str):
  user = {
      "id": 1,
      "name": "John Doe",
      "email": "email",
      "password": "password"
  }
  entity = UserOut(**user)
  return entity

@router.put("/user/profile", response_model=UserIn)
async def update_profle():
    return Response(status_code=status.HTTP_200_OK)
