
from typing import List
from dto.ticket import TicketRequest, TicketResponse
from models.ticket import Ticket
from sqlalchemy.orm import Session


def search(db: Session) -> List[TicketResponse]:
  tickets = db.query(Ticket).all()
  response = []
  for ticket in tickets:
    response.append(TicketResponse(
      id=ticket.id,
      title=ticket.title,
      description=ticket.description,
      user_id=ticket.user_id,
      price=ticket.price,
      slot=ticket.slot,
      created_at=ticket.created_at,
      updated_at=ticket.updated_at
    ))
  return response
