from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from app.schema.unit_schema import UnitBase

if TYPE_CHECKING:
    from .sensor_model import Sensor

class Unit(UnitBase, table=True):
    __tablename__ = "units"
    id: int | None = Field(primary_key=True, index=True, default=None)

    sensors: list["Sensor"] = Relationship(back_populates="unit")  # pyright: ignore[reportUndefinedVariable]