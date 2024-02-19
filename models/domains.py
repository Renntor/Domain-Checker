from sqlalchemy import Column, Integer, String, Date
from config.database import Base


class Domain(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    created = Column(Date)
    expiry_date = Column(Date)
