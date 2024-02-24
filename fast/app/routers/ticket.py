from typing import List
from fastapi import APIRouter, Response, Depends, status
from query_service.ticket import search
from sqlalchemy.orm import Session
from depends import get_db
import dto

router = APIRouter()

@router.get("/",response_model=List[dto.TicketResponse])
async def show(db: Session = Depends(get_db)):
    response = search(db)
    return response

@router.get("/{ticket_id}/")
async def pick(ticket_id: int):
    return {"ticket_id": ticket_id}

@router.put("/{ticket_id}")
async def update(ticket_id):
    return Response(status_code=status.HTTP_200_OK)

@router.post("/")
async def create():
    return Response(status_code=status.HTTP_200_OK)

@router.delete("/{ticket_id}/")
async def delete(ticket_id):
    return Response(status_code=status.HTTP_200_OK)