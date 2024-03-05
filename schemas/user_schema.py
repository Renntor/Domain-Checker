from pydantic import BaseModel
from schemas.links_schema import Links


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    link: Links

    class Config:
        orm_mode = True

