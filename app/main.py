from fastapi import FastAPI
from app.api import car
from app.db.database import Base, engine
from app.models import car as car_model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Monitoring Innovation API")

app.include_router(car.router)
