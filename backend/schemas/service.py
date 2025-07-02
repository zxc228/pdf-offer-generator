from pydantic import BaseModel

class ServiceRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

    class Config:
        orm_mode = True

class ServiceCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
