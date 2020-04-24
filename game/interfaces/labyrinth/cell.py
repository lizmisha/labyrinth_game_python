from abc import ABCMeta, abstractmethod
from typing import Tuple


class Cell(metaclass=ABCMeta):

    @abstractmethod
    def action(self, command: str) -> Tuple[str, Tuple[int, int]]: pass
