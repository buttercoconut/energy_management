from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.schemas import UserCreate, User
from ..auth.auth import authenticate_user, create_token_response, get_current_user, get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return create_token_response(user)

@router.post("/users", response_model=User)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # Simple user creation for demo
    hashed_pw = authenticate_user.get_password_hash(user_in.password)
    user = User(username=user_in.username, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
