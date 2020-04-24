from abc import ABCMeta, abstractmethod
from typing import Callable, Tuple

from game.interfaces.player import Player


class GameAction(metaclass=ABCMeta):

    @abstractmethod
    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]: pass
