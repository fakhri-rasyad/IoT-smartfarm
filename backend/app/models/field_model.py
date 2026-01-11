from sqlmodel import SQLModel, Field

class FarmField(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    user_id : int = Field(foreign_key="user.id")

    esps: list["ESP"] = Relationship(back_populates="field")  # pyright: ignore[reportUndefinedVariable]
    
    user: "User" = Relationship(back_populates="fields")  # pyright: ignore[reportUndefinedVariable]