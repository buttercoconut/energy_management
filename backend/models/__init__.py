"""Database models for the Energy Management system.

All tables are defined using SQLAlchemy ORM. The Base class is imported from
`database.session` so that migrations can be generated with Alembic if needed.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Integer, default=1)

    # Relationships
    consumptions = relationship("Consumption", back_populates="user")
    alerts = relationship("Alert", back_populates="user")

class EnergySource(Base):
    __tablename__ = "energy_sources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)  # e.g., solar, wind, grid
    capacity_kw = Column(Float, nullable=False)

    consumptions = relationship("Consumption", back_populates="source")

class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    source_id = Column(Integer, ForeignKey("energy_sources.id"))
    timestamp = Column(DateTime, nullable=False)
    amount_kwh = Column(Float, nullable=False)

    user = relationship("User", back_populates="consumptions")
    source = relationship("EnergySource", back_populates="consumptions")

class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("energy_sources.id"))
    forecast_time = Column(DateTime, nullable=False)
    predicted_kwh = Column(Float, nullable=False)

    source = relationship("EnergySource")

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="alerts")
