from fastapi import APIRouter
from fastapi import Response
from fastapi import status

router = APIRouter()


@router.post("/login")
async def login(email: str, password: str):
    return Response(status_code=status.HTTP_200_OK)


@router.get("/logout")
async def logout():
    return Response(status_code=status.HTTP_200_OK)
  
  
@router.get("/sign_up")
async def sign_up():
    return Response(status_code=status.HTTP_200_OK)
  
  
@router.get("/sign_out")
async def sign_out():
    return Response(status_code=status.HTTP_200_OK)
  
  
@router.get("/password_reset")
async def password_reset():
    return Response(status_code=status.HTTP_200_OK)