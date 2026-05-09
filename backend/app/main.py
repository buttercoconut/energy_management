# FastAPI application entry point

from fastapi import FastAPI
from .routes import router as energy_router
from .database import engine
from .models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Energy Management API")

app.include_router(energy_router)

# Simple health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
