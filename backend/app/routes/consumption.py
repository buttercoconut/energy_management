from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/consumptions", tags=["consumptions"])

@router.post("/", response_model=schemas.EnergyConsumption)
async def create_consumption(consumption: schemas.EnergyConsumptionCreate, db: Session = Depends(get_db)):
    db_consumption = models.EnergyConsumption(**consumption.dict())
    db.add(db_consumption)
    db.commit()
    db.refresh(db_consumption)
    return db_consumption

@router.get("/", response_model=list[schemas.EnergyConsumption])
async def read_consumptions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    consumptions = db.query(models.EnergyConsumption).offset(skip).limit(limit).all()
    return consumptions
