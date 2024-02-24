
from pydantic import BaseModel


class BaseEntity(BaseModel):
    def to_dict(self):
        return self.model_dump()