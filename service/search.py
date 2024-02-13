from abc import ABC, abstractmethod


class Domain(ABC):

    def __init__(self, domain):
        self.domain = domain

    @abstractmethod
    def search(self, name):
        pass

    @abstractmethod
    def package(self):
        pass


class DomainRU(Domain):

    def search(self, name):
        pass

    def package(self):
        pass



