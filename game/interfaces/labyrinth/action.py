from abc import ABCMeta, abstractmethod


class Action(metaclass=ABCMeta):

    @abstractmethod
    def execute(self): pass
