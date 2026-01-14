from fastapi import APIRouter
from app.schema.user_schema import UserCreate, UserPublic

user_router = APIRouter(prefix="/users", tags=["users_route"])

@user_router.get("/", response_model=list[UserPublic])
async def get_all_users():
    return {}

@user_router.get("/{user_id}", response_model=UserPublic)
async def get_user(user_id: int):
    return {}

@user_router.post("/", response_model=UserPublic)
async def create_user(user_data: UserCreate):
    return {}


@user_router.patch("/{user_id}", response_model=UserPublic)
async def update_user(user_id: int):
    return {}

@user_router.delete("/{user_id}")
async def delete_user(user_id:int):
    return {}