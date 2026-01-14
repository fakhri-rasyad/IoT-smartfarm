from fastapi import APIRouter
from app.schema.unit_schema import UnitCreate, UnitPublic

unit_router = APIRouter(prefix="/units", tags=["units_route"])

@unit_router.get("/", response_model=list[UnitPublic])
async def get_all_units():
    return {}

@unit_router.get("/{unit_id}", response_model=UnitPublic)
async def get_unit(unit_id: int):
    return {}

@unit_router.post("/", response_model=UnitPublic)
async def create_unit(unit_data: UnitCreate):
    return {}


@unit_router.patch("/{unit_id}", response_model=UnitPublic)
async def update_unit(unit_id: int):
    return {}

@unit_router.delete("/{unit_id}")
async def delete_unit(unit_id:int):
    return {}