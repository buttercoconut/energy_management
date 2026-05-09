from .database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    sensors = relationship("Sensor", back_populates="building")

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    building = relationship("Building", back_populates="sensors")
    consumptions = relationship("EnergyConsumption", back_populates="sensor")

class EnergyConsumption(Base):
    __tablename__ = "energy_consumptions"
    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    energy_kwh = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    sensor = relationship("Sensor", back_populates="consumptions")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="viewer")
