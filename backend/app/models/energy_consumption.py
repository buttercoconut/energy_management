from pydantic import BaseModel
from datetime import datetime

class EnergyConsumption(BaseModel):
    id: int
    building_id: int
    sensor_id: int
    timestamp: datetime
    consumption_kwh: float
