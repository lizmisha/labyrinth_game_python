from typing import Tuple

from game.interfaces.player import Player, Bear
from labyrinth.implementations.constants import PLAYER_HEALTH
from labyrinth.implementations.visualize_constants import SYM_BEAR, SYM_PLAYER


class PlayerBase(Player):

    def __init__(
            self,
            coordinates: Tuple[int, int],
            treasure: bool = False,
            icon: str = SYM_PLAYER,
            player_health: int = PLAYER_HEALTH
    ):
        self.treasure = treasure
        self.player_icon = icon
        self.coordinates = coordinates
        self.player_health = player_health

    @property
    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates

    @property
    def have_treasure(self) -> bool:
        return self.treasure

    @property
    def icon(self) -> str:
        return self.player_icon

    @property
    def health(self) -> int:
        return self.player_health

    def damage(self):
        self.player_health = self.player_health - 1 if self.player_health > 0 else 0


class BearBase(Bear):

    def __init__(self, coordinates: Tuple[int, int], treasure: bool = False, icon: str = SYM_BEAR):
        self.treasure = treasure
        self.player_icon = icon
        self.coordinates = coordinates

    @property
    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates

    @property
    def have_treasure(self) -> bool:
        return False

    @property
    def icon(self) -> str:
        return self.player_icon
