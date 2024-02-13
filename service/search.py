import re
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import httpx


class Domain(ABC):

    url = 'https://who.is/whois/'

    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def search(self, name):
        pass

    @abstractmethod
    def package(self):
        pass


class DomainRU(Domain):

    def __init__(self, name):
        self.name = name

    def search(self):
        data = httpx.get(self.url + self.name, timeout=200.0).text
        if '504 Gateway' in data:
            return None
        soup = BeautifulSoup(data, 'lxml').find(class_='col-md-12 queryResponseBodyValue').text
        text_search = re.findall(r'paid-till:     \d{4}-\d\d-\d\d', soup)[0][14:]
        return text_search

    def package(self):
        pass



x = DomainRU('ya.ru')

print(x.search())
