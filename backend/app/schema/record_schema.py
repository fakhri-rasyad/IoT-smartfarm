from sqlmodel import SQLModel, Field
from datetime import datetime
from app.core.utils.utils import utc_now

class RecordBase(SQLModel):
    timestamp: datetime = Field(index=True, default_factory=utc_now)
    value: float

class RecordCreate(RecordBase):
    sensor_id: int

class RecordPublic(RecordBase):
    id: int
    sensor_id: int
