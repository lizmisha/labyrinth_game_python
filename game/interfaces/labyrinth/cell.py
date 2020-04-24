from abc import ABCMeta, abstractmethod
from typing import Tuple

from game.interfaces.player import Player


class Cell(metaclass=ABCMeta):

    @abstractmethod
    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]: pass

    @property
    @abstractmethod
    def is_isolated(self) -> bool: pass
