from fastapi import APIRouter
from app.schema.field_schema import FieldPublic, FieldCreate

field_router = APIRouter(prefix="/fields", tags=["field_route"])

@field_router.get("/", response_model=list[FieldPublic])
async def get_all_field():
    return {}

@field_router.get("/{route_id}", response_model=list[FieldPublic])
async def get_all_field(field_id: int):
    return {}

@field_router.post("/", response_model=FieldPublic)
async def create_field(field_data: FieldCreate):
    return {}

@field_router.patch("/{route_id}", response_model=FieldPublic)
async def update_field(field_id: int):
    return {}

@field_router.delete("/field_id")
async def delete_field(field_id: int):
    return {}