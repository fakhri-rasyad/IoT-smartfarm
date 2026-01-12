from sqlmodel import SQLModel
from app.schema.role_schema import RolePublic

class UserBase(SQLModel):
    name: str

class UserCreate(UserBase):
    email: str
    password: str
    role_id: int

class UserPublic(UserBase):
    id: int
    email:str

class UserPublicWithRole(UserPublic):
    role: RolePublic | None = None