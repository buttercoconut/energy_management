from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import services, auth as auth_module
from ..database import get_db

router = APIRouter(prefix="/analysis", tags=["analysis"])

@router.get("/predict/{building_id}")
async def predict(building_id: int, days: int = 1, db: Session = Depends(get_db), current_user: auth_module.models.User = Depends(auth_module.get_current_user)):
    service = services.energy_analysis.EnergyAnalysisService(db)
    preds = service.predict_next(building_id, days)
    if preds is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not enough data")
    return {"predictions": preds}

@router.get("/report/{building_id}")
async def report(building_id: int, month: int, year: int, db: Session = Depends(get_db), current_user: auth_module.models.User = Depends(auth_module.get_current_user)):
    generator = services.report_generation.ReportGenerator(db)
    report = generator.generate_monthly_report(building_id, month, year)
    return report
