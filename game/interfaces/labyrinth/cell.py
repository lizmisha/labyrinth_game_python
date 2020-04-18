from abc import ABCMeta, abstractmethod


class Cell(metaclass=ABCMeta):

    @abstractmethod
    def action(self): pass
