from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import users
from config.database import engine, SessionLocal
from schemas.user import User, UserCreate
from routers import crud_user
from service.utils import verify_password


users.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already used')
    return crud_user.create_user(db=db, user=user)


@app.get('/users/', response_model=list[User])
async def read_users(db: Session = Depends(get_db)):
    users = crud_user.get_users(db)
    return users


@app.get('/users/{email}/', response_model=User)
async def read_user(email: str, password: str, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    hash_password = db_user.password
    if not verify_password(password, hash_password):
        raise HTTPException(status_code=400, detail='Email or password is wrong')
    return db_user
