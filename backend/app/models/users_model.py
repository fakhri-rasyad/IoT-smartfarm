from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password:str 
    role_id: int | None = Field(default=None, foreign_key="role.id")

    role : "Role" | None = Relationship(back_populates="users")  # pyright: ignore[reportUndefinedVariable]