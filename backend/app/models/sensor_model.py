from sqlmodel import SQLModel, Field, Relationship

class Sensor(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    esp_id: int = Field(foreign_key="esp.id", index=True)
    unit_id: int = Field(foreign_key="unit.id", index=True)
    type_id : int = Field(foreign_key="sensortype.id", index=True)

    unit: "Unit" = Relationship(back_populates="sensors")  # pyright: ignore[reportUndefinedVariable]
    type: "SensorType" = Relationship(back_populates="sensors")  # pyright: ignore[reportUndefinedVariable]
    esp: "ESP" = Relationship(back_populates="sensors")  # pyright: ignore[reportUndefinedVariable]

    records: list["Record"] = Relationship(back_populates="sensor")  # pyright: ignore[reportUndefinedVariable]