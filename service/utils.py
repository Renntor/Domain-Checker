from passlib.context import CryptContext
from service.search import DomainRU, DomainCOM


domain_dict = {'ru': DomainRU, 'com': DomainCOM}

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(password: str, hashed_password: str) -> bool:
    """
    password verification
    :param password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(password, hashed_password)


def searching(domain: str):
    """
    Domain searching
    :param domain:
    :return:
    """
    # top-level domain
    tld = domain.split('.')[-1]
    if tld in domain_dict:
        return domain_dict[tld]().search_data(domain)
    else:
        return None

