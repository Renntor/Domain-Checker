from pydantic import BaseModel


class Links(BaseModel):
    id: int
    user: int
    domain_id: int

    class Config:
        orm_mode = True

