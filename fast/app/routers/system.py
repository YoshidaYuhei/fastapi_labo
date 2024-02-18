from fastapi import APIRouter
from fastapi import Response
from fastapi import status

router = APIRouter()


@router.get("/healthcheck")
async def get_healthcheck():
    return Response(status_code=status.HTTP_200_OK)
