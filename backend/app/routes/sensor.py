from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/sensors", tags=["sensors"])

@router.post("/", response_model=schemas.Sensor)
async def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    db_sensor = models.Sensor(name=sensor.name, type=sensor.type, building_id=sensor.building_id)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

@router.get("/", response_model=list[schemas.Sensor])
async def read_sensors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sensors = db.query(models.Sensor).offset(skip).limit(limit).all()
    return sensors
