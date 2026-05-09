from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..models.building import Building
from ..services.energy_analysis import EnergyAnalysisService
from ..dependencies import get_db

router = APIRouter(prefix="/buildings", tags=["buildings"])

@router.get("/", response_model=List[Building])
async def list_buildings(db: Session = Depends(get_db)):
    return db.query(Building).all()

@router.post("/", response_model=Building, status_code=status.HTTP_201_CREATED)
async def create_building(building: Building, db: Session = Depends(get_db)):
    db.add(building)
    db.commit()
    db.refresh(building)
    return building

# Additional CRUD endpoints can be added similarly
