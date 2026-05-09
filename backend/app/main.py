from fastapi import FastAPI
from .routes import token as token_router, energy_consumption as energy_router
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Energy Management API")

app.include_router(token_router.router)
app.include_router(energy_router.router)

# Simple health check
@app.get("/health")
def health():
    return {"status": "ok"}
