from fastapi import APIRouter, HTTPException
from ..models.energy_consumption import EnergyConsumption
from typing import List

router = APIRouter()

# In-memory store for demo purposes
store: List[EnergyConsumption] = []

@router.post("/", response_model=EnergyConsumption)
async def create_consumption(data: EnergyConsumption):
    store.append(data)
    return data

@router.get("/", response_model=List[EnergyConsumption])
async def list_consumptions():
    return store
