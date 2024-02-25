from typing import Union
import datetime
from fastapi import Query

from pydantic import Field

from dto.abstract import BaseDto

class TicketOption(BaseDto):
    id: int
    ticket_id: int
    descirption: Union[str, None] = None
    price: int = Field(gt=0)

class BaseTicket(BaseDto):
    id: int
    title: str
    description: Union[str, None] = Field(
        default=None, title="The description of the ticket", max_length=300
    )
    price: float = Field(gt=0, default=0, examples=[200, 100], description="The price must be greater than zero")
    options: Union[list[TicketOption], None] = None
    
class TicketResponse(BaseTicket):
    created_at: Union[datetime.datetime, None] = datetime.datetime.utcnow()
    updated_at: Union[datetime.datetime, None] = datetime.datetime.utcnow()
