from sqlmodel import SQLModel, Field

class SensorType(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    description: str | None = None

    sensors: list["Sensor"] = Relationship(back_populates="type")  # pyright: ignore[reportUndefinedVariable]