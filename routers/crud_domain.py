from sqlalchemy.orm import Session
from models.domains import Domain
from schemas.domain_schema import DomainCreate
from service.utils import searching


def get_domain(db: Session, domain: str):
    return db.query(Domain).filter(Domain.name == domain).first()


def create_domain(db: Session, domain: DomainCreate):
    result = searching(domain.name)
    if result is not None:
        db_domain = Domain(name=domain.name, created=result[0], expiry_date=result[1])
        db.add(db_domain)
        db.commit()
        db.refresh(db_domain)
        return db_domain
    else:
        return None
