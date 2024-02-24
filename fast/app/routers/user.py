from fastapi import APIRouter, Response, status

from entity import UserRequest

router = APIRouter()


# @router.get("/profile", response_model=UserOut)
# async def get_profile(email: str, password: str):
#   user = {
#       "id": 1,
#       "name": "John Doe",
#       "email": "email",
#       "password": "password"
#   }
#   return entity

# @router.put("/profile", response_model=)
# async def update_profle():
#     return Response(status_code=status.HTTP_200_OK)
