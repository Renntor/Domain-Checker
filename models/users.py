from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    link = relationship('Link', backref='links', uselist=False)
