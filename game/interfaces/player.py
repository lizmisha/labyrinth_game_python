from abc import ABCMeta, abstractmethod
from typing import Tuple


class Player(metaclass=ABCMeta):

    @abstractmethod
    @property
    def get_coordinates(self) -> Tuple[int, int]: pass

    @abstractmethod
    @property
    def have_treasure(self) -> bool: pass
