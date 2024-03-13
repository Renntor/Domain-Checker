from pydantic import BaseModel


class CreateLinks(BaseModel):
    user: int


class Links(CreateLinks):
    id: int
    domain_id: int

    class Config:
        orm_mode = True


