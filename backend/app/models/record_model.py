from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class Record(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    sensor_id: int = Field(foreign_key="sensor.id", index=True)
    timestamp: datetime = Field(index=True, default_factory=datetime.now(timezone.utc))
    value: float

    sensor: "Sensor" = Relationship(back_populates="records")  # pyright: ignore[reportUndefinedVariable]