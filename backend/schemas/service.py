from pydantic import BaseModel

class ServiceBase(BaseModel):
    name: str
    description: str | None = None

class ServiceCreate(ServiceBase):
    pass

class ServiceRead(ServiceBase):
    id: int

    class Config:
        orm_mode = True
