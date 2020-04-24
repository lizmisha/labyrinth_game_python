import random
from typing import List

from game.interfaces.labyrinth.labyrinth import StandardLabyrinth
from game.implementations.labyrinth.labyrinth import Labyrinth
from game.implementations.labyrinth.cells import CellBase, make_monolith_cell
from game.implementations.labyrinth.constants import (BOUND_SIZE, TREASURE_COUNT, EXITS_COUNT, WORMHOLES_COUNT,
                                                      ACTIONS2FROM)


class LabyrinthFactory:

    def __init__(
            self,
            size: int,
            treasure_count: int = TREASURE_COUNT,
            wormholes_count: int = WORMHOLES_COUNT,
            exits_count: int = EXITS_COUNT
    ):
        assert BOUND_SIZE[0] <= size <= BOUND_SIZE[1],\
            f'Size should be not less {BOUND_SIZE[0]} and not bigger {BOUND_SIZE[1]}'

        self.size = (size, size)
        self.treasure_count = treasure_count
        self.wormholes_count = wormholes_count
        self.exits_count = exits_count

    def _generate_cells(self) -> List[List[CellBase]]:
        cells = []
        for row in range(self.size[0]):
            cells_row = []
            for column in range(self.size[1]):
                curr_cell = CellBase()
                if row == 0 or column == 0:
                    curr_cell = make_monolith_cell(curr_cell)

                cells_row.append(curr_cell)

            cells.append(cells_row)

        return cells

    def _get_random_coordinates(self):
        y = random.choice(range(1, self.size[0] - 2))
        x = random.choice(range(1, self.size[1] - 2))
        return y, x

    def generate(self) -> StandardLabyrinth:
        cells = self._generate_cells()
        labyrinth = Labyrinth(cells)

        init_y, init_x = self._get_random_coordinates()
        cell = labyrinth.cells[init_y][init_x]

        visited_cells_num = 1
        cells_stack = []

        return labyrinth
