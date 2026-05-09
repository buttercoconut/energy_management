# Pydantic schemas for API

from datetime import datetime
from pydantic import BaseModel, Field

class DataPointCreate(BaseModel):
    meter_id: int
    timestamp: datetime
    energy_kwh: float

class DataPointOut(BaseModel):
    id: int
    meter_id: int
    timestamp: datetime
    energy_kwh: float

    class Config:
        orm_mode = True

class EnergyMeterCreate(BaseModel):
    building_id: int
    serial_number: str
    type: str

class EnergyMeterOut(BaseModel):
    id: int
    building_id: int
    serial_number: str
    type: str

    class Config:
        orm_mode = True

class BuildingCreate(BaseModel):
    name: str
    location: str | None = None

class BuildingOut(BaseModel):
    id: int
    name: str
    location: str | None = None

    class Config:
        orm_mode = True
