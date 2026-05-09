from pydantic import BaseModel, Field
from datetime import datetime

class Building(BaseModel):
    id: int = Field(..., description="Unique identifier for the building")
    name: str = Field(..., description="Name of the building")
    location: str = Field(..., description="Geographical location or address")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
