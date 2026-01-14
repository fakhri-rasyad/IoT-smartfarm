from sqlmodel import SQLModel, Field
from app.schema.esp_schema import ESPPublic
from app.schema.user_schema import UserPublic

class FieldBase(SQLModel):
    name: str

class FieldCreate(FieldBase):
    user_id: int
    pass

class FieldPublic(FieldBase):
    id: int
    user_id:int

class FieldPublicWithUser(FieldPublic):
    user: UserPublic | None = None

class FieldPublicWithEsp(FieldPublic):
    esps: list[ESPPublic] = []