from fastapi import APIRouter
from ..services.energy_analysis import predict_energy

router = APIRouter()

@router.get("/predict")
async def get_prediction(hours: int = 24):
    # Dummy data for demo
    data = [i for i in range(hours)]
    prediction = predict_energy(data)
    return {"prediction": prediction}
