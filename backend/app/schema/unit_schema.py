from sqlmodel import SQLModel
from app.schema.sensor_schema import SensorPublic

class UnitBase(SQLModel):
    name: str
    symbol: str

class UnitCreate(UnitBase):
    pass

class UnitPublic(UnitBase):
    id: int

class UnitPublicWithSensor(UnitPublic):
    sensors: list[SensorPublic] = []