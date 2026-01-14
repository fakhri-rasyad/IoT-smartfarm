from fastapi import FastAPI
from app.routes import *

app = FastAPI()

app.include_router(esp_router)
app.include_router(field_router)
app.include_router(record_router)
app.include_router(role_router)
app.include_router(sensor_router)
app.include_router(sensor_type_router)
app.include_router(unit_router)
app.include_router(user_router)