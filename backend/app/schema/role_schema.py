from sqlmodel import SQLModel
from typing import Optional

class RoleBase(SQLModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RolePublic(RoleBase):
    id: int