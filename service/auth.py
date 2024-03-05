from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from config.database import SessionLocal
from routers import crud_user
from service.utils import pwd_context, verify_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.user_schema import UserCreate


load_dotenv()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




router = APIRouter(prefix='/auth', tags=['auth'])


SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class Token(BaseModel):
    access_token: str
    token_type: str


db_dependency = Annotated[Session, Depends(get_db)]


@router.post('/token', response_model=Token)
async def login(from_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    users = authenticate_user(from_data.username, from_data.password, db)
    if not users:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    token = create_access_token(users.email, users.id, timedelta(minutes=20))

    return {'access_token': token}


def authenticate_user(email: str, password: str, db):
    db_user = crud_user.get_user_by_email(db, email=email)
    if db_user is None:
        return False
    hash_password = db_user.password
    if not verify_password(password, hash_password):
        return False
    return db_user


def create_access_token(user_email: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': user_email, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
