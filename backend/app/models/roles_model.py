from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from app.schema.role_schema import RoleBase

if TYPE_CHECKING:
    from .users_model import User

class Role(RoleBase, table=True):
    __tablename__ = "roles"
    id: int | None = Field(default=None, primary_key=True)

    users: list["User"] = Relationship(back_populates="role") # pyright: ignore[reportUndefinedVariable]