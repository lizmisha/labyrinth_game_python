from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):

    @abstractmethod
    def start(self): pass
