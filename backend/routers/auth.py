"""Router for authentication endpoints.

For simplicity this example uses a very basic token scheme. In a real
application you would use OAuth2 with JWTs.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.session import SessionLocal
from crud import create_user, get_user_by_username
from schemas import UserCreate, UserOut

router = APIRouter()

# Dependency to get DB session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
async def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    user = create_user(db, user_in)
    return user

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or user.hashed_password != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # In a real app return a JWT
    return {"access_token": user.username, "token_type": "bearer"}
