from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    sensors = relationship("Sensor", back_populates="building")
    consumptions = relationship("EnergyConsumption", back_populates="building")

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    serial = Column(String, unique=True, index=True)
    type = Column(String)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    building = relationship("Building", back_populates="sensors")
    consumptions = relationship("EnergyConsumption", back_populates="sensor")

class EnergyConsumption(Base):
    __tablename__ = "energy_consumptions"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True)
    value = Column(Float)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    building = relationship("Building", back_populates="consumptions")
    sensor = relationship("Sensor", back_populates="consumptions")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
