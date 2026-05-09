from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..crud.crud import get_device, create_device
from ..schemas.schemas import DeviceCreate, Device
from ..auth.auth import get_current_active_user

router = APIRouter(prefix="/devices", tags=["devices"])

@router.post("/", response_model=Device, status_code=status.HTTP_201_CREATED)
async def create_new_device(device: DeviceCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return create_device(db, device, owner_id=current_user.id)

@router.get("/{device_id}", response_model=Device)
async def read_device(device_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_device = get_device(db, device_id)
    if db_device is None or db_device.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device
