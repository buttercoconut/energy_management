from pydantic import BaseModel, Field
from datetime import datetime

class Sensor(BaseModel):
    id: int = Field(..., description="Unique identifier for the sensor")
    building_id: int = Field(..., description="Foreign key to Building")
    type: str = Field(..., description="Sensor type (e.g., electricity, water, gas)")
    location: str = Field(..., description="Physical location of the sensor")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
