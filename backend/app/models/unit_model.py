from sqlmodel import SQLModel, Field

class Unit(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    symbol: str

    sensors: list["Sensor"] = Relationship(back_populates="unit")  # pyright: ignore[reportUndefinedVariable]