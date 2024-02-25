from typing import Annotated, Any, List, Union
from MySQLdb import Time
from fastapi import APIRouter, Path, Query, Response, Depends, status 
from query_service.ticket import search
from sqlalchemy.orm import Session
from depends import get_db
from dto import BaseTicket, TicketResponse

router = APIRouter()

@router.get("/",response_model=List[TicketResponse])
async def show(db: Session = Depends(get_db)):
    response = search(db)
    return response

@router.get("/{ticket_id}/", response_model=TicketResponse)
async def pick(ticket_id: int) -> BaseTicket:
    return TicketResponse(id=ticket_id, title='title')

@router.put("/{ticket_id}", response_model=None)
async def update(ticket_id: int, request: BaseTicket):
    return { "ticket_id": ticket_id, "request": request}

@router.post("/", response_model=TicketResponse)
async def create(request: BaseTicket) -> Any:
    return request

@router.delete("/{ticket_id}/")
async def delete(ticket_id):
    return Response(status_code=status.HTTP_200_OK)