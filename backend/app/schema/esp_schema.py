from sqlmodel import SQLModel
from app.enum.device_status import DeviceStatus

class ESPBase(SQLModel):
    mac_address: str 
    status: DeviceStatus = DeviceStatus.ONLINE

class ESPCreate(ESPBase):
    user_id: int
    field_id: int
    pass

class ESPPublic(ESPBase):
    id: int

class ESPUpdate(ESPBase):
    status: DeviceStatus | None = None
    field_id: int | None = None
    user_id:int | None = None