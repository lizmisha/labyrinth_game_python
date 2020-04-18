from abc import ABCMeta, abstractmethod


class StandardLabyrinth(metaclass=ABCMeta):

    @abstractmethod
    def execute_action(self): pass
