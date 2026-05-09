from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    username: str = Field(..., description="Login username")
    email: str = Field(..., description="User email address")
    role: str = Field(..., description="Role (e.g., admin, manager, engineer)")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
