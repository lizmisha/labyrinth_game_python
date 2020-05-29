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

    @abstractmethod
    def damage(self): pass

    @property
    @abstractmethod
    def health(self) -> int: pass


class Bear(metaclass=ABCMeta):

    @property
    @abstractmethod
    def get_coordinates(self) -> Tuple[int, int]: pass

    @property
    @abstractmethod
    def have_treasure(self) -> bool: pass

    @property
    @abstractmethod
    def icon(self) -> str: pass
