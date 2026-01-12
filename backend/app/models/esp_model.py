from sqlmodel import SQLModel, Field, Enum, Column, Relationship
from app.enum.device_status import DeviceStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sensor_model import Sensor
    from .users_model import User
    from .field_model import FarmField

class ESP(SQLModel, table=True):
    __tablename__ = "esps"

    id: int | None = Field(primary_key=True, index=True, default=None)
    mac_address: str = Field(index=True, unique=True)
    status: DeviceStatus = Field(default=DeviceStatus.OFFLINE, sa_column=Column(Enum(DeviceStatus)))
    field_id: int | None = Field(default=None, foreign_key="farmfields.id", index=True)
    user_id: int | None = Field(default=None, foreign_key="users.id", index=True)

    field: "FarmField" = Relationship(back_populates="esps")  # pyright: ignore[reportUndefinedVariable]
    user:  "User" = Relationship(back_populates="esps")  # pyright: ignore[reportUndefinedVariable]
    
    sensors: list["Sensor"] = Relationship(back_populates="esp")  # pyright: ignore[reportUndefinedVariable]
