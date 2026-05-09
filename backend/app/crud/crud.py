from sqlalchemy.orm import Session
from .models import User, Device, Sensor, Reading
from ..schemas.schemas import UserCreate, DeviceCreate, SensorCreate, ReadingCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User CRUD

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Device CRUD

def get_device(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()

def create_device(db: Session, device: DeviceCreate, owner_id: int):
    db_device = Device(**device.dict(), owner_id=owner_id)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

# Sensor CRUD

def get_sensor(db: Session, sensor_id: int):
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

def create_sensor(db: Session, sensor: SensorCreate, owner_id: int):
    db_sensor = Sensor(**sensor.dict(), owner_id=owner_id)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

# Reading CRUD

def create_reading(db: Session, reading: ReadingCreate):
    db_reading = Reading(**reading.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading
