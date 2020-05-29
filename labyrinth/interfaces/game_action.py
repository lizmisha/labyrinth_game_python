from abc import ABCMeta, abstractmethod
from typing import Callable, Tuple, Union

from game.interfaces.player import Player, Bear


class GameAction(metaclass=ABCMeta):

    @abstractmethod
    def execute_action(
            self,
            player: Union[Player, Bear],
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]: pass

    @abstractmethod
    def show_command(self, command: str) -> str: pass
