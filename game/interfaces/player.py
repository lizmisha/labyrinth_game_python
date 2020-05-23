from abc import ABCMeta, abstractmethod
from typing import Tuple


class Player(metaclass=ABCMeta):

    @property
    @abstractmethod
    def get_coordinates(self) -> Tuple[int, int]: pass

    @property
    @abstractmethod
    def have_treasure(self) -> bool: pass

    @property
    @abstractmethod
    def icon(self) -> str: pass
