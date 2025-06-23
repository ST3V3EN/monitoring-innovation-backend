from pydantic import BaseModel

class CarBase(BaseModel):
    Marca: str
    Sucursal: str
    Aspirante: str

class CarCreate(CarBase):
    pass

class CarRead(CarBase):
    Id: int

class Config:
    from_attributes = True
