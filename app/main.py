from fastapi import FastAPI
from app.controller import car
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Monitoring Innovation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car.router)