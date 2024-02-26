from pydantic import BaseModel
from datetime import date


class DomainCreate(BaseModel):
    name: str


class Domain(DomainCreate):
    id: int
    created: date
    expiry_date: date

    class Config:
        orm_mode = True
