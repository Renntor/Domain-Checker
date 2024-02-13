from pydantic import BaseModel
from datetime import date


class Domain(BaseModel):

    name: str
    created: date
    expiry_date: date

    class Config:
        orm_mode = True
