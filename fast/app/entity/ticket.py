from typing import Union
import datetime
from fastapi import Query

from pydantic import Field

from entity.abstract import BaseEntity

class TicketOption(BaseEntity):
    ticket_id: int
    descirption: Union[str, None] = None
    price: int = Field(gt=0)

class BaseTicket(BaseEntity):
    title: str
    description: Union[str, None] = Field(
        default=None, title="The description of the ticket", max_length=300
    )
    price: float = Field(gt=0, default=0, examples=[200, 100], description="The price must be greater than zero")
    
class TicketCreateIn(BaseTicket):
    created_at: Union[datetime.datetime, None] = datetime.datetime.utcnow()
    updated_at: Union[datetime.datetime, None] = datetime.datetime.utcnow()
