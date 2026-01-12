from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .esp_model import ESP
    from .sensor_type_model import SensorType
    from .unit_model import Unit
    from .record_model import Record

class Sensor(SQLModel, table=True):
    __tablename__ = "sensors"

    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    esp_id: int = Field(foreign_key="esps.id", index=True)
    unit_id: int = Field(foreign_key="units.id", index=True)
    type_id : int = Field(foreign_key="sensortypes.id", index=True)

    unit: "Unit" = Relationship(back_populates="sensors")  # pyright: ignore[reportUndefinedVariable]
    type: "SensorType" = Relationship(back_populates="sensors")  # pyright: ignore[reportUndefinedVariable]
    esp: "ESP" = Relationship(back_populates="sensors")  # pyright: ignore[reportUndefinedVariable]

    records: list["Record"] = Relationship(back_populates="sensor")  # pyright: ignore[reportUndefinedVariable]