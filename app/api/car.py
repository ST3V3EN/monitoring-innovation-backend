from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.car import CarCreate, CarRead
from app.services import car

router = APIRouter(prefix="/cars", tags=["cars"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CarRead)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    return car.create_car(db, car)

@router.get("/", response_model=list[CarRead])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return car.get_cars(db, skip, limit)

@router.get("/{car_id}", response_model=CarRead)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = car.get_car(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.delete("/{car_id}", response_model=CarRead)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = car.delete_car(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
