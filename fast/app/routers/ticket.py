from typing import List, Union
from fastapi import APIRouter, Response, Depends, status
from query_service.ticket import search
from sqlalchemy.orm import Session
from depends import get_db
from dto import TicketRequest, TicketResponse

router = APIRouter()

@router.get("/",response_model=List[TicketResponse])
async def show(db: Session = Depends(get_db)):
    response = search(db)
    return response

@router.get("/{ticket_id}/")
async def pick(request: TicketRequest):
    return request

@router.put("/{ticket_id}")
async def update(ticket_id: int, request: TicketRequest):
    return { "ticket_id": ticket_id, **request.model_dump() }

@router.post("/")
async def create(request: TicketRequest):
    dic = request.model_dump()
    return dic

@router.delete("/{ticket_id}/")
async def delete(ticket_id):
    return Response(status_code=status.HTTP_200_OK)