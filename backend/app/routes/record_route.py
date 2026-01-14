from fastapi import APIRouter
from app.schema.record_schema import RecordCreate, RecordPublic

record_router = APIRouter(prefix="/records", tags=["records_route"])

@record_router.get("/", response_model=list[RecordPublic])
async def get_all_records():
    return {}

@record_router.get("/{record_id}", response_model=RecordPublic)
async def get_one_record(record_id: int):
    return {}

@record_router.post("/", response_model=RecordPublic)
async def insert_record(record_data: RecordCreate):
    return {}

@record_router.patch("/{record_id}", response_model=RecordPublic)
async def update_record(record_id: int):
    return {}

@record_router.delete("/{record_id}")
async def delete_record(record_id: int):
    return {}