from typing import Tuple

from game.interfaces.player import Player
from game.implementations.labyrinth.visualize_constants import sym_player


class PlayerBase(Player):

    def __init__(self, coordinates: Tuple[int, int], treasure: bool = False, icon: str = sym_player):
        self.treasure = treasure
        self.player_icon = icon
        self.coordinates = coordinates

    @property
    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates

    @property
    def have_treasure(self) -> bool:
        return self.treasure

    @property
    def icon(self) -> str:
        return self.player_icon
