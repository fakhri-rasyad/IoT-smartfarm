from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sensor_model import Sensor

class Record(SQLModel, table=True):
    __tablename__ = "records"

    id: int | None = Field(primary_key=True, index=True, default=None)
    timestamp: datetime = Field(index=True, default_factory=datetime.now(timezone.utc))
    value: float
    
    sensor_id: int = Field(foreign_key="sensors.id", index=True)

    sensor: "Sensor" = Relationship(back_populates="records")  # pyright: ignore[reportUndefinedVariable]