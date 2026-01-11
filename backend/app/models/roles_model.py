from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Role(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

    users: list["User"] = Relationship(back_populates="role") # pyright: ignore[reportUndefinedVariable]