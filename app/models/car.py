from sqlalchemy import Column, Integer, String
from ..db.database import Base

class Car(Base):
    __tablename__ = "Car"

    Id = Column(Integer, primary_key=True, index=True)
    Marca = Column(String, index=True)
    Sucursal = Column(String, unique=True, index=True)
    Aspirante = Column(String, unique=True, index=True)