from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from config.database import Base


link_domain = Table('link_domain', Base.metadata,
                    Column('link_id', Integer, ForeignKey('domains.id')),
                    Column('domain_id', Integer, ForeignKey('links.id'))
                    )


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    user = Column(Integer(), ForeignKey('users.id'))
    domain_id = Column(Integer(), ForeignKey('domains.id'))
    domain = relationship('Domain', secondary=link_domain, backref='domains')