"""CRUD operations for the Energy Management system.

Each function receives a SQLAlchemy session and performs the required
database interaction. The functions are intentionally simple to keep the
example focused on the API layer.
"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from models import User, EnergySource, Consumption, Forecast, Alert
from schemas import (
    UserCreate,
    EnergySourceCreate,
    ConsumptionCreate,
    ForecastCreate,
    AlertCreate,
)

# User CRUD

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=user_in.password,  # In production hash the password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# EnergySource CRUD

def get_source(db: Session, source_id: int) -> Optional[EnergySource]:
    return db.query(EnergySource).filter(EnergySource.id == source_id).first()


def create_source(db: Session, source_in: EnergySourceCreate) -> EnergySource:
    source = EnergySource(**source_in.dict())
    db.add(source)
    db.commit()
    db.refresh(source)
    return source

# Consumption CRUD

def create_consumption(db: Session, consumption_in: ConsumptionCreate, user_id: int) -> Consumption:
    consumption = Consumption(
        user_id=user_id,
        source_id=consumption_in.source_id,
        timestamp=consumption_in.timestamp,
        amount_kwh=consumption_in.amount_kwh,
    )
    db.add(consumption)
    db.commit()
    db.refresh(consumption)
    return consumption


def get_consumptions(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Consumption]:
    return (
        db.query(Consumption)
        .filter(Consumption.user_id == user_id)
        .order_by(Consumption.timestamp.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

# Forecast CRUD

def create_forecast(db: Session, forecast_in: ForecastCreate) -> Forecast:
    forecast = Forecast(**forecast_in.dict())
    db.add(forecast)
    db.commit()
    db.refresh(forecast)
    return forecast

# Alert CRUD

def create_alert(db: Session, user_id: int, message: str) -> Alert:
    alert = Alert(user_id=user_id, message=message, created_at=datetime.utcnow())
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert

# Additional CRUD functions can be added as needed.
