from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..crud.crud import create_reading
from ..schemas.schemas import ReadingCreate, Reading
from ..auth.auth import get_current_active_user

router = APIRouter(prefix="/readings", tags=["readings"])

@router.post("/", response_model=Reading, status_code=status.HTTP_201_CREATED)
async def create_new_reading(reading: ReadingCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return create_reading(db, reading)
