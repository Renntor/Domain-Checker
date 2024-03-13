from pydantic import BaseModel
from sqlalchemy.orm import Mapped, relationship

from schemas.links_schema import CreateLinks


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    link: CreateLinks

    class Config:
        orm_mode = True

