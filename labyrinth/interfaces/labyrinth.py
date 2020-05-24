from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from game.interfaces.player import Player


class StandardLabyrinth(metaclass=ABCMeta):

    @abstractmethod
    def execute_command(self, command: str, player: Player) -> Tuple[bool, str]: pass

    @property
    @abstractmethod
    def get_empty_cells(self) -> List[Tuple[int, int]]: pass

    @abstractmethod
    def put_player_icon(self, icon: str, coordinates: Tuple[int, int]): pass

    @abstractmethod
    def show_map(self): pass
