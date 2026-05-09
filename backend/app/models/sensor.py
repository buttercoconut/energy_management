from .database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    building = relationship("Building", back_populates="sensors")
    consumptions = relationship("EnergyConsumption", back_populates="sensor")
