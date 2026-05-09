from pydantic import BaseModel, Field
from datetime import datetime

class EnergyConsumption(BaseModel):
    id: int = Field(..., description="Unique identifier for the record")
    building_id: int = Field(..., description="Foreign key to Building")
    sensor_id: int = Field(..., description="Foreign key to Sensor")
    timestamp: datetime = Field(..., description="Timestamp of the reading")
    consumption_kwh: float = Field(..., description="Energy consumption in kWh")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
