from pydantic import BaseModel, Field

class CarCreate(BaseModel):
    marca: str = Field(..., min_length=1, max_length=50)
    sucursal: str = Field(..., min_length=1, max_length=50)
    aspirante: str = Field(..., min_length=1, max_length=50)

class CarRead(BaseModel):
    id: int
    marca: str
    sucursal: str
    aspirante: str
