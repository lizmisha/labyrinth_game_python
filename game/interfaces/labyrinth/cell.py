from abc import ABCMeta, abstractmethod
from typing import Tuple

from game.interfaces.player import Player


class Cell(metaclass=ABCMeta):

    @abstractmethod
    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]: pass

    @property
    @abstractmethod
    def get_coordinates(self): pass

    @abstractmethod
    def show_cell(self): pass
