from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/buildings", tags=["buildings"])

@router.post("/", response_model=schemas.Building)
async def create_building(building: schemas.BuildingCreate, db: Session = Depends(get_db)):
    db_building = models.Building(name=building.name, location=building.location)
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

@router.get("/", response_model=list[schemas.Building])
async def read_buildings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    buildings = db.query(models.Building).offset(skip).limit(limit).all()
    return buildings
