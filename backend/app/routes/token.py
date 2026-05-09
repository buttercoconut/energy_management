from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session
from .. import auth as auth_module
from ..database import get_db

router = APIRouter()

@router.post("/token", response_model=auth_module.schemas.token.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(auth_module.models.User).filter(auth_module.models.User.username == form_data.username).first()
    if not user or user.hashed_password != auth_module.fake_hash_password(form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=auth_module.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_module.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return auth_module.schemas.token.Token(access_token=access_token, token_type="bearer")
