from pydantic import BaseModel, Field
from datetime import datetime

class EnergyConsumptionCreate(BaseModel):
    timestamp: datetime
    value: float
    building_id: int
    sensor_id: int

class EnergyConsumptionRead(EnergyConsumptionCreate):
    id: int

    class Config:
        orm_mode = True
