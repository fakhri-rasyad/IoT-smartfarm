from sqlmodel import SQLModel, Field, Enum, Column
from app.enum.device_status import DeviceStatus

class ESP(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    mac_address: str = Field(index=True, unique=True)
    field_id: int | None = Field(default=None, foreign_key="farmfield.id", index=True)
    user_id: int | None = Field(default=None, foreign_key="user.id", index=True)
    status: DeviceStatus = Field(default=DeviceStatus.OFFLINE, sa_column=Column(Enum(DeviceStatus)), index=True)

    field: "FarmField" | None = Relationship(back_populates="esps")  # pyright: ignore[reportUndefinedVariable]
    user:  "User" | None = Relationship(back_populates="esps")  # pyright: ignore[reportUndefinedVariable]
    
    sensors: list["Sensor"] = Relationship(back_populates="esp")  # pyright: ignore[reportUndefinedVariable]
