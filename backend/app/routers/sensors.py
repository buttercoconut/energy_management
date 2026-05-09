from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..crud.crud import get_sensor, create_sensor
from ..schemas.schemas import SensorCreate, Sensor
from ..auth.auth import get_current_active_user

router = APIRouter(prefix="/sensors", tags=["sensors"])

@router.post("/", response_model=Sensor, status_code=status.HTTP_201_CREATED)
async def create_new_sensor(sensor: SensorCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return create_sensor(db, sensor, owner_id=current_user.id)

@router.get("/{sensor_id}", response_model=Sensor)
async def read_sensor(sensor_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_sensor = get_sensor(db, sensor_id)
    if db_sensor is None or db_sensor.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor
