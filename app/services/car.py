import logging
from app.db.database import get_db_connection
from app.schemas.car import CarCreate
from app.schemas.car import CarRead 

async def create_table_service():
    conn = await get_db_connection()
    if conn is None:
        return False
    try:
        async with conn.transaction():
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS Car (
                    Id SERIAL PRIMARY KEY,
                    Marca TEXT NOT NULL,
                    Sucursal TEXT NOT NULL,
                    Aspirante TEXT NOT NULL
                );
            """)
            return True
    except Exception as e:
        logging.error(f"Error creating table: {e}")
        return False
    finally:
        await conn.close()

async def get_car(conn, car_id: int):
    try:
        result = await conn.fetchrow("SELECT * FROM Car WHERE id = $1", car_id)
        return dict(result) if result else None
    except Exception as e:
        logging.error(f"Error getting car: {e}")
        raise

async def get_cars(conn, skip: int = 0, limit: int = 10):
    try:
        results = await conn.fetch("SELECT * FROM Car OFFSET $1 LIMIT $2", skip, limit)
        return [dict(row) for row in results]
    except Exception as e:
        logging.error(f"Error getting cars: {e}")
        raise

async def create_car(conn, car_data: CarCreate):
    try:
        async with conn.transaction():
            result = await conn.fetchrow("""
                INSERT INTO Car (marca, sucursal, aspirante)
                VALUES ($1, $2, $3)
                RETURNING id, marca, sucursal, aspirante
            """, car_data.marca, car_data.sucursal, car_data.aspirante)
            return dict(result)
    except Exception as e:
        logging.error(f"Error creating car: {e}")
        raise

async def update_car_service(car_id: int, car_data: CarCreate):
    try:
        conn = await get_db_connection()
        async with conn.transaction():
            result = await conn.execute(
                """
                UPDATE Car
                SET marca = $1, sucursal = $2, aspirante = $3
                WHERE id = $4
                RETURNING *;
                """,
                car_data.marca, car_data.sucursal, car_data.aspirante, car_id
            )
            updated = await conn.fetchrow("SELECT * FROM Car WHERE id = $1", car_id)

            if updated:
                return CarRead(**dict(updated))
            return None
    except Exception as e:
        logging.error(f"An error occurred while updating: {e}")
        raise
    finally:
        if conn:
            await conn.close()

async def delete_car(conn, car_id: int):
    try:
        async with conn.transaction():
            result = await conn.fetchrow("""
                DELETE FROM car WHERE id = $1
                RETURNING id, marca, sucursal, aspirante
            """, car_id)
            return dict(result) if result else None
    except Exception as e:
        logging.error(f"Error deleting car: {e}")
        raise