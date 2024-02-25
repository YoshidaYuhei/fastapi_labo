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

class TicketRequest(BaseDto):
    id: int
    description: Union[str, None] = Field(
        default=None, title="The description of the ticket", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    # options: Union[list[TicketOption], None] = None
    
    def query_extractor(self, id: int = Query(None), description: str = Query(None), price: float = Query(None)):
        return TicketRequest(id=id, description=description, price=price)

class TicketResponse(BaseDto):
    id: int
    title: str
    description: Union[str, None] = None
    user_id: int
    price: int
    slot: float
    created_at: datetime.datetime
    updated_at: datetime.datetime
