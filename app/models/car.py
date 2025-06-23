from pydantic import BaseModel, constr

class Car(BaseModel):
    marca: constr(min_length=1, max_length=50)
    sucursal: constr(min_length=1, max_length=50)
    aspirante: constr(min_length=1, max_length=50)