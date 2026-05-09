from pydantic import BaseModel, Field
from datetime import datetime

class BuildingBase(BaseModel):
    name: str
    location: Optional[str] = None

class BuildingCreate(BuildingBase):
    pass

class Building(BuildingBase):
    id: int
    class Config:
        orm_mode = True
