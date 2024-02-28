from typing import Annotated, Any, List, Union
from MySQLdb import Time
from fastapi import APIRouter, Path, Query, Response, Depends, status 
from sqlalchemy.orm import Session
from depends.get_db import get_db
from dto import TicketOut
from entity import TicketCreateIn

router = APIRouter()

@router.get("/",response_model=List[TicketOut])
async def show(db: Session = Depends(get_db)):
    return "test"

# @router.get("/{ticket_id}/", response_model=TicketResponse)
# async def pick(ticket_id: int) -> BaseTicket:
#     return TicketResponse(id=ticket_id, title='title')

# @router.put("/{ticket_id}", response_model=None)
# async def update(ticket_id: int, request: BaseTicket):
#     return { "ticket_id": ticket_id, "request": request}

# @router.post("/", response_model=None)
# async def create(request: TicketCreateIn):
    
#     return True

# @router.delete("/{ticket_id}/")
# async def delete(ticket_id):
#     return Response(status_code=status.HTTP_200_OK)