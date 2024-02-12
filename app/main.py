from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import users
from config.database import engine, SessionLocal
from schemas.user import User, UserCreate
from routers import crud_user
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
users.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already used')
    user.password = pwd_context.hash(user.password)
    return crud_user.create_user(db=db, user=user)


@app.get('/users/', response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    users = crud_user.get_users(db)
    return users


@app.get('/users/{user_id}/items/', response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user
