from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users_model import User
    from .esp_model import ESP

class FarmField(SQLModel, table=True):
    __tablename__ = "farmfields"

    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    user_id : int = Field(foreign_key="users.id")

    esps: list["ESP"] = Relationship(back_populates="field")  # pyright: ignore[reportUndefinedVariable]
    
    user: "User" = Relationship(back_populates="fields")  # pyright: ignore[reportUndefinedVariable]