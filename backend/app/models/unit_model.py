from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sensor_model import Sensor

class Unit(SQLModel, table=True):
    __tablename__ = "units"
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    symbol: str

    sensors: list["Sensor"] = Relationship(back_populates="unit")  # pyright: ignore[reportUndefinedVariable]