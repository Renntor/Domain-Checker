from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.users import User
from schemas.user_schema import UserCreate
from schemas.links_schema import CreateLinks

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=password)
    print(db_user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
