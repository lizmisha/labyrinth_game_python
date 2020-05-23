from abc import ABCMeta, abstractmethod
from typing import Tuple

from game.interfaces.player import Player
from game.implementations.labyrinth.visualize_constants import sym_monolith


class Cell(metaclass=ABCMeta):

    def __init__(self):
        self.game_actions = dict()
        self.cell_center = ' '

    @abstractmethod
    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int], bool]: pass

    @property
    @abstractmethod
    def get_coordinates(self) -> Tuple[int, int]: pass

    @property
    @abstractmethod
    def is_isolated(self) -> bool: pass

    @abstractmethod
    def show_cell(self) -> Tuple[str, str, str, str, str]: pass
    

class CellMonolith(metaclass=ABCMeta):

    def __init__(self):
        self.game_actions = dict()
        self.cell_center = sym_monolith

    @abstractmethod
    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int], bool]: pass

    @property
    @abstractmethod
    def get_coordinates(self) -> Tuple[int, int]: pass

    @abstractmethod
    def show_cell(self) -> Tuple[str, str, str, str, str]: pass
