from fastapi import APIRouter
from app.schema.sensor_type_schema import SensorTypeCreate, SensorTypePublic

sensor_type_router = APIRouter(prefix="/sensor_types", tags=["sensor_types_route"])

@sensor_type_router.get("/", response_model=list[SensorTypePublic])
async def get_all_sensor_types():
    return {}

@sensor_type_router.get("/{sensor_type_id}", response_model=SensorTypePublic)
async def get_sensor_type(sensor_type_id: int):
    return {}

@sensor_type_router.post("/", response_model=SensorTypePublic)
async def create_sensor_type(sensor_type_data: SensorTypeCreate):
    return {}


@sensor_type_router.patch("/{sensor_type_id}", response_model=SensorTypePublic)
async def update_sensor_type(sensor_type_id: int):
    return {}

@sensor_type_router.delete("/{sensor_type_id}")
async def delete_sensor_type(sensor_type_id:int):
    return {}