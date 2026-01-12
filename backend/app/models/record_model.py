from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING
from app.schema.record_schema import RecordBase

if TYPE_CHECKING:
    from .sensor_model import Sensor

class Record(RecordBase, table=True):
    __tablename__ = "records"

    id: int | None = Field(primary_key=True, index=True, default=None)
    
    sensor_id: int = Field(foreign_key="sensors.id", index=True)

    sensor: "Sensor" = Relationship(back_populates="records")  # pyright: ignore[reportUndefinedVariable]