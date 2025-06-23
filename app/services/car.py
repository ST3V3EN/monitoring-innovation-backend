from sqlalchemy.orm import Session
from app.models import car
from app.schemas import car

def create_car(db: Session, car: car.CarCreate):
    db_car = car.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_car(db: Session, car_id: int):
    return db.query(car.Car).filter(car.Car.Id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(car.Car).offset(skip).limit(limit).all()

def delete_car(db: Session, car_id: int):
    car = db.query(car.Car).filter(car.Car.Id == car_id).first()
    if car:
        db.delete(car)
        db.commit()
    return car
