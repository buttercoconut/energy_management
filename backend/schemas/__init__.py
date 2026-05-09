"""Pydantic schemas for request/response validation.

Each schema corresponds to a database model but only exposes the fields that
are relevant for API consumers.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# EnergySource schemas
class EnergySourceBase(BaseModel):
    name: str
    type: str
    capacity_kw: float

class EnergySourceCreate(EnergySourceBase):
    pass

class EnergySourceOut(EnergySourceBase):
    id: int

    class Config:
        orm_mode = True

# Consumption schemas
class ConsumptionBase(BaseModel):
    source_id: int
    timestamp: datetime
    amount_kwh: float

class ConsumptionCreate(ConsumptionBase):
    pass

class ConsumptionOut(ConsumptionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Forecast schemas
class ForecastBase(BaseModel):
    source_id: int
    forecast_time: datetime
    predicted_kwh: float

class ForecastCreate(ForecastBase):
    pass

class ForecastOut(ForecastBase):
    id: int

    class Config:
        orm_mode = True

# Alert schemas
class AlertBase(BaseModel):
    message: str

class AlertCreate(AlertBase):
    pass

class AlertOut(AlertBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
