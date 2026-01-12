from sqlmodel import SQLModel
from app.schema.sensor_schema import SensorPublic

class SensorTypeBase(SQLModel):
    name: str
    description: str | None = None

class SensorTypeCreate(SensorTypeBase):
    pass

class SensorTypePublic(SensorTypeBase):
    id: int

class SensorTypeWithSensor(SensorTypePublic):
    sensors: list[SensorPublic] = []
