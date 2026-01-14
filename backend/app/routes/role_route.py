from fastapi import APIRouter
from app.schema.role_schema import RoleCreate, RolePublic

role_router = APIRouter(prefix="/roles", tags=["roles_route"])

@role_router.get("/", response_model=list[RolePublic])
async def get_all_roles():
    return {}

@role_router.get("/{role_id}", response_model=RolePublic)
async def get_role(role_id: int):
    return {}

@role_router.post("/", response_model=RolePublic)
async def create_role(role_data: RoleCreate):
    return {}


@role_router.patch("/{role_id}", response_model=RolePublic)
async def update_role(role_id: int):
    return {}

@role_router.delete("/{role_id}")
async def delete_role(role_id:int):
    return {}