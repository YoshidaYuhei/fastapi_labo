import datetime
from fastapi import FastAPI
from pydantic import BaseModel

from dto.abstract import BaseDto

class TicketRequest(BaseDto):
    id: int

class TicketResponse(BaseDto):
    id: int
    title: str
    description: str
    user_id: int
    price: int
    slot: float
    created_at: datetime.datetime
    updated_at: datetime.datetime
