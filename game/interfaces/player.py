from abc import ABCMeta, abstractmethod
from typing import Tuple


class Player(metaclass=ABCMeta):

    def __init__(self):
        self.have_treasure = False

    @property
    @abstractmethod
    def get_coordinates(self) -> Tuple[int, int]: pass
