from sqlmodel import SQLModel, Field
from app.schema.esp_schema import ESPPublic

class FieldBase(SQLModel):
    name: str

class FieldCreate(FieldBase):
    user_id: int
    pass

class FieldPublic(FieldBase):
    id: int
    user_id:int

class FieldPublicWithUser(FieldPublic):
    # Ill add this after creating UserPublic
    pass

class FieldPublicWithEsp(FieldPublic):
    esps: list[ESPPublic] = []