from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db_connection
from app.schemas.car import CarCreate, CarRead
from app.services import car

router = APIRouter(prefix="/cars", tags=["cars"])

async def get_conn():
    conn = await get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    try:
        yield conn
    finally:
        await conn.close()

@router.post("/createTable")
async def create_table():
    success = await car.create_table_service()
    if not success:
        raise HTTPException(status_code=500, detail="Table creation failed")
    return {"message": "Table created successfully"}

@router.get("/{car_id}", response_model=CarRead)
async def read_car(car_id: int, conn=Depends(get_conn)):
    db_car = await car.get_car(conn, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.get("/", response_model=list[CarRead])
async def read_cars(skip: int = 0, limit: int = 10, conn=Depends(get_conn)):
    return await car.get_cars(conn, skip, limit)

@router.post("/", response_model=CarRead)
async def create_car(car_data: CarCreate, conn=Depends(get_conn)):
    return await car.create_car(conn, car_data)

@router.put("/{car_id}", response_model=CarRead)
async def update_car(car_id: int, car_data: CarCreate):
    updated_car = await car.update_car_service(car_id, car_data)
    if not updated_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated_car

@router.delete("/{car_id}", response_model=CarRead)
async def delete_car(car_id: int, conn=Depends(get_conn)):
    db_car = await car.delete_car(conn, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
