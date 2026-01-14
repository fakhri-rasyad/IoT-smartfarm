from fastapi import APIRouter
from app.schema.sensor_schema import SensorCreate, SensorPublic

sensor_router = APIRouter(prefix="/sensors", tags=["sensors_route"])

@sensor_router.get("/", response_model=list[SensorPublic])
async def get_all_sensors():
    return {}

@sensor_router.get("/{sensor_id}", response_model=SensorPublic)
async def get_sensor(sensor_id: int):
    return {}

@sensor_router.post("/", response_model=SensorPublic)
async def create_sensor(sensor_data: SensorCreate):
    return {}


@sensor_router.patch("/{sensor_id}", response_model=SensorPublic)
async def update_sensor(sensor_id: int):
    return {}

@sensor_router.delete("/{sensor_id}")
async def delete_sensor(sensor_id:int):
    return {}