import random
from typing import Tuple

from game.interfaces.player import Player
from game.interfaces.labyrinth.labyrinth import StandardLabyrinth
from game.implementations.labyrinth.visualize_constants import sym_player


class PlayerBase(Player):

    def __init__(self, labyrinth: StandardLabyrinth):
        super().__init__()

        self.coordinates = self._create(labyrinth)

    def _create(self, labyrinth: StandardLabyrinth) -> Tuple[int, int]:
        idx = random.choice(range(len(labyrinth.empty_cells)))
        cell_coord = labyrinth.empty_cells[idx]
        labyrinth.cells[cell_coord[0]][cell_coord[1]].cell_center = sym_player
        return cell_coord

    @property
    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates
