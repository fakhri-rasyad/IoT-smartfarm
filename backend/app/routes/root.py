from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
async def read_root():
    return {"message" :  "Welcome to the IoT Smart Farm API"}