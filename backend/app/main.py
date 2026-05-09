from fastapi import FastAPI
from .routes import building, energy_consumption, user

app = FastAPI(title="Energy Management API")

app.include_router(building.router, prefix="/buildings", tags=["buildings"])
app.include_router(energy_consumption.router, prefix="/energy", tags=["energy"])
app.include_router(user.router, prefix="/users", tags=["users"])
