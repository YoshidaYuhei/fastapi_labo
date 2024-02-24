from typing import Union
import datetime

from dto.abstract import BaseDto

class TicketRequest(BaseDto):
    id: int
    description: Union[str, None] = None

class TicketResponse(BaseDto):
    id: int
    title: str
    description: Union[str, None] = None
    user_id: int
    price: int
    slot: float
    created_at: datetime.datetime
    updated_at: datetime.datetime
