from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def save(self, filename: str): pass

    @abstractmethod
    def game(self): pass
