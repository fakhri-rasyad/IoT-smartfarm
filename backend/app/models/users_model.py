from sqlmodel import SQLModel, Field, Relationship
from app.models.roles_model import Role
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .roles_model import Role

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password:str 
    role_id: int | None = Field(default=None, foreign_key="roles.id")

    role : Optional["Role"] | None = Relationship(back_populates="users")  # pyright: ignore[reportUndefinedVariable]