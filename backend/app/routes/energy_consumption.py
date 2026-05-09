from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..models.energy_consumption import EnergyConsumption
from ..dependencies import get_db

router = APIRouter(prefix="/energy", tags=["energy"])

@router.get("/consumption", response_model=List[EnergyConsumption])
async def get_consumption(db: Session = Depends(get_db)):
    return db.query(EnergyConsumption).all()

@router.post("/consumption", response_model=EnergyConsumption, status_code=status.HTTP_201_CREATED)
async def add_consumption(consumption: EnergyConsumption, db: Session = Depends(get_db)):
    db.add(consumption)
    db.commit()
    db.refresh(consumption)
    return consumption

# Endpoint for prediction
from ..services.energy_analysis import EnergyAnalysisService

@router.post("/predict", response_model=float)
async def predict_consumption(building_id: int, timestamp: str, db: Session = Depends(get_db)):
    service = EnergyAnalysisService(db)
    return service.predict(building_id, timestamp)
