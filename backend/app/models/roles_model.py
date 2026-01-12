from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .users_model import User

class Role(SQLModel, table=True):
    __tablename__ = "roles"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

    users: list["User"] = Relationship(back_populates="role") # pyright: ignore[reportUndefinedVariable]