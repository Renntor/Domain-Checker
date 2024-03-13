from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from config.database import Base
from models.domains import Domain


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    link: Mapped["Link"] = relationship('Link', back_populates='user')

class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    user: Mapped["User"] = relationship('User', back_populates='link')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    domain_id = Column(Integer(), ForeignKey('domains.id'), nullable=True)