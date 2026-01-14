from fastapi import APIRouter
from app.schema.esp_schema import ESPPublic, ESPCreate, ESPUpdate

esp_router = APIRouter(prefix="/esps", tags=["esp_route"])

@esp_router.get("/", response_model=list[ESPPublic])
async def get_all_esp():
    return {}

@esp_router.get("/{esp_id}", response_model=ESPPublic)
async def get_esp_by_id(esp_id: int):
    return {}

@esp_router.get("/{route_mac}/mac_address")
async def get_esp_by_mac(mac_id: str):
    return {}

@esp_router.post("/", response_model=ESPPublic)
async def create_esp(esp_data: ESPCreate):
    return {}

@esp_router.patch("/{esp_id}", response_model=ESPPublic)
async def update_esp(esp_data: ESPUpdate):
    return {}

@esp_router.delete("/{esp_id}")
async def delete_esp(esp_id: int):
    return {}