from abc import ABCMeta, abstractmethod

from game.interfaces.player import Player


class StandardLabyrinth(metaclass=ABCMeta):

    def __init__(self):
        self.cells = []
        self.empty_cells = []

    @abstractmethod
    def execute_command(self, command: str, player: Player): pass

    @abstractmethod
    def show_map(self): pass
