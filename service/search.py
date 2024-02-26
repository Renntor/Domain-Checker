import re
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import httpx


class Domain(ABC):

    url = 'https://who.is/whois/'

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def search_data(self):
        pass


class DomainRU(Domain):

    def __init__(self, name):
        self.name = name

    def search_data(self):
        data = httpx.get(self.url + self.name, timeout=200.0).text
        if '504 Gateway' in data:
            return None
        soup = BeautifulSoup(data, 'lxml').find(style='border:0px;').text
        experi_date = re.findall(r'paid-till:     \d{4}-\d\d-\d\d', soup)[0][15:]
        created_date = re.findall(r'created:       \d{4}-\d\d-\d\d', soup)[0][15:]
        return created_date, experi_date


class DomainCOM(Domain):

    def __init__(self, name):
        self.name = name

    def search_data(self):
        data = httpx.get(self.url + self.name, timeout=200.0).text
        if '504 Gateway' in data:
            return None
        soup = BeautifulSoup(data, 'lxml').find_all(class_='col-md-8 queryResponseBodyValue')[4:6]
        return soup[1].text, soup[0].text

