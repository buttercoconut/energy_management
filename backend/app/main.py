from fastapi import FastAPI
from .routes import building, energy_consumption, user

app = FastAPI(title="Energy Management API")

app.include_router(building.router)
app.include_router(energy_consumption.router)
app.include_router(user.router)

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
