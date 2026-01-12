from sqlmodel import SQLModel
from app.schema.record_schema import RecordPublic

class SensorBase(SQLModel):
    name: str

class SensorCreate(SensorBase):
    esp_id: int
    unit_id: int
    type_id: int

class SensorPublic(SensorBase):
    id: int
    esp_id: int
    unit_id: int
    type_id: int

class SensorPublicWithRecords(SensorPublic):
    records: list[RecordPublic] = []