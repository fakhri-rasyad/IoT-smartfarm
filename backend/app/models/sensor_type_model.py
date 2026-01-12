from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from app.schema.sensor_type_schema import SensorTypeBase

if TYPE_CHECKING:
    from .sensor_model import Sensor

class SensorType(SensorTypeBase, table=True):
    __tablename__ = "sensortypes"
    id: int | None = Field(primary_key=True, index=True, default=None)
    sensors: list["Sensor"] = Relationship(back_populates="type")  # pyright: ignore[reportUndefinedVariable]