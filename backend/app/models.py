# SQLAlchemy models for Energy Management System

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    location = Column(String)
    meters = relationship("EnergyMeter", back_populates="building")

class EnergyMeter(Base):
    __tablename__ = "energy_meters"
    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    serial_number = Column(String, unique=True, nullable=False)
    type = Column(String)
    building = relationship("Building", back_populates="meters")
    data_points = relationship("DataPoint", back_populates="meter")

class DataPoint(Base):
    __tablename__ = "data_points"
    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(Integer, ForeignKey("energy_meters.id"))
    timestamp = Column(DateTime, nullable=False)
    energy_kwh = Column(Float, nullable=False)
    meter = relationship("EnergyMeter", back_populates="data_points")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="viewer")

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    building_id = Column(Integer, ForeignKey("buildings.id"))
    created_at = Column(DateTime)
    content = Column(String)
