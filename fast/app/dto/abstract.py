
from pydantic import BaseModel


class BaseDto(BaseModel):
    def to_dict(self):
        return self.model_dump()