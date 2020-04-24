from abc import ABCMeta, abstractmethod

from game.interfaces.player import Player


class StandardLabyrinth(metaclass=ABCMeta):

    @abstractmethod
    def execute_command(self, command: str, player: Player): pass
