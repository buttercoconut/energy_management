from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models, schemas, auth as auth_module
from ..database import get_db

router = APIRouter(prefix="/energy", tags=["energy"])

@router.post("/consumption", response_model=schemas.energy_consumption.EnergyConsumptionRead)
def create_consumption(consumption: schemas.energy_consumption.EnergyConsumptionCreate, db: Session = Depends(get_db), current_user: auth_module.models.User = Depends(auth_module.get_current_user)):
    # Basic validation
    if consumption.timestamp > datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Timestamp cannot be in the future")
    db_consumption = models.EnergyConsumption(**consumption.dict())
    db.add(db_consumption)
    db.commit()
    db.refresh(db_consumption)
    return db_consumption

@router.get("/consumption", response_model=list[schemas.energy_consumption.EnergyConsumptionRead])
def read_consumptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth_module.models.User = Depends(auth_module.get_current_user)):
    consumptions = db.query(models.EnergyConsumption).offset(skip).limit(limit).all()
    return consumptions
