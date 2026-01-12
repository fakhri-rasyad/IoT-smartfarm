from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sensor_model import Sensor

class SensorType(SQLModel, table=True):
    __tablename__ = "sensortypes"
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    description: str | None = None

    sensors: list["Sensor"] = Relationship(back_populates="type")  # pyright: ignore[reportUndefinedVariable]