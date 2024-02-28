from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)
