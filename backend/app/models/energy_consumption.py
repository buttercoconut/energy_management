from .database import Base
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class EnergyConsumption(Base):
    __tablename__ = "energy_consumptions"
    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    energy_kwh = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    sensor = relationship("Sensor", back_populates="consumptions")
