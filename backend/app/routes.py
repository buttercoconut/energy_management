# FastAPI routes for energy meters and data points

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api", tags=["energy"])

# Energy Meter CRUD
@router.post("/meters", response_model=schemas.EnergyMeterOut)
async def create_meter(meter: schemas.EnergyMeterCreate, db: Session = Depends(get_db)):
    db_meter = models.EnergyMeter(**meter.dict())
    db.add(db_meter)
    db.commit()
    db.refresh(db_meter)
    return db_meter

@router.get("/meters/{meter_id}", response_model=schemas.EnergyMeterOut)
async def read_meter(meter_id: int, db: Session = Depends(get_db)):
    db_meter = db.query(models.EnergyMeter).filter(models.EnergyMeter.id == meter_id).first()
    if not db_meter:
        raise HTTPException(status_code=404, detail="Meter not found")
    return db_meter

# Data Point CRUD
@router.post("/data", response_model=schemas.DataPointOut)
async def create_data_point(dp: schemas.DataPointCreate, db: Session = Depends(get_db)):
    db_dp = models.DataPoint(**dp.dict())
    db.add(db_dp)
    db.commit()
    db.refresh(db_dp)
    return db_dp

@router.get("/data/{meter_id}", response_model=list[schemas.DataPointOut])
async def get_data_points(meter_id: int, start: datetime | None = None, end: datetime | None = None, db: Session = Depends(get_db)):
    query = db.query(models.DataPoint).filter(models.DataPoint.meter_id == meter_id)
    if start:
        query = query.filter(models.DataPoint.timestamp >= start)
    if end:
        query = query.filter(models.DataPoint.timestamp <= end)
    return query.all()
