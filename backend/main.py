"""Main entry point for the Energy Management backend.

This module sets up the FastAPI application, includes routers, and configures
database connections. It follows a modular structure so that each domain
(e.g. energy, consumption, forecast, alerts) can be developed independently.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routers.energy import router as energy_router
from routers.consumption import router as consumption_router
from routers.forecast import router as forecast_router
from routers.alerts import router as alerts_router
from routers.auth import router as auth_router

# Import database session
from database.session import SessionLocal, engine
from models import Base

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Energy Management API",
    description="API for managing energy consumption, forecasting, and alerts.",
    version="0.1.0",
)

# CORS configuration – allow all origins for demo purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(energy_router, prefix="/energy", tags=["energy"])
app.include_router(consumption_router, prefix="/consumption", tags=["consumption"])
app.include_router(forecast_router, prefix="/forecast", tags=["forecast"])
app.include_router(alerts_router, prefix="/alerts", tags=["alerts"])

# Dependency to get DB session
@app.middleware("http")
async def db_session_middleware(request, call_next):
    request.state.db = SessionLocal()
    try:
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Simple health check
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}
