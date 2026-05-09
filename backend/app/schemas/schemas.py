from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class DeviceBase(BaseModel):
    name: str

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class SensorBase(BaseModel):
    type: str

class SensorCreate(SensorBase):
    device_id: int

class Sensor(SensorBase):
    id: int
    device_id: int

    class Config:
        orm_mode = True

class ReadingBase(BaseModel):
    value: str

class ReadingCreate(ReadingBase):
    sensor_id: int

class Reading(ReadingBase):
    id: int
    sensor_id: int

    class Config:
        orm_mode = True
