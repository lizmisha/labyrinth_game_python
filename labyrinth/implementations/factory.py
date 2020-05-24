import random
from typing import List, Tuple, Union

from labyrinth.interfaces.cell import Cell, CellMonolith
from labyrinth.interfaces.labyrinth import StandardLabyrinth
from labyrinth.implementations.labyrinth import Labyrinth
from labyrinth.implementations.cells import CellBase, CellMonolithBase
from labyrinth.implementations.cells_utils import (get_cell_neighbors, connect_cells, make_exit, make_treasure,
                                                   make_wormholes, make_river)
from labyrinth.implementations.constants import (BOUND_SIZE, TREASURE_COUNT, EXITS_COUNT, WORMHOLES_COUNT,
                                                 RIVERS_COUNT, BOUND_RIVER_LEN, RIVER_MAKE_CHANCES)


class LabyrinthFactory:

    def __init__(
            self,
            size: int,
            rivers_count: int = RIVERS_COUNT,
            rivers_bound: Tuple[int, int] = BOUND_RIVER_LEN,
            treasure_count: int = TREASURE_COUNT,
            wormholes_count: int = WORMHOLES_COUNT,
            exits_count: int = EXITS_COUNT
    ):
        assert BOUND_SIZE[0] <= size <= BOUND_SIZE[1],\
            f'Size should be not less {BOUND_SIZE[0]} and not bigger {BOUND_SIZE[1]}'

        self.size = (size, size)
        self.rivers_count = rivers_count
        self.rivers_bound = rivers_bound
        self.treasure_count = treasure_count
        self.wormholes_count = wormholes_count
        self.exits_count = exits_count

    def _generate_cells(self) -> Tuple[List[List[Union[Cell, CellMonolith]]], List[Tuple[int, int]]]:
        cells = []
        empty_cells = []
        for row in range(self.size[0]):
            cells_row = []
            for column in range(self.size[1]):
                if (row == 0) or (row == self.size[0] - 1) or (column == 0) or (column == self.size[1] - 1):
                    curr_cell = CellMonolithBase(coordinates=(row, column))
                else:
                    curr_cell = CellBase(coordinates=(row, column))
                    empty_cells.append((row, column))

                cells_row.append(curr_cell)
            cells.append(cells_row)

        return cells, empty_cells

    def _get_random_coordinates(self):
        y = random.choice(range(1, self.size[0] - 2))
        x = random.choice(range(1, self.size[1] - 2))
        return y, x

    def _generate_rivers(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        for _ in range(self.rivers_count):
            river_len = random.choice(range(self.rivers_bound[0], self.rivers_bound[1] + 1))
            is_make = False
            for _ in range(RIVER_MAKE_CHANCES):
                is_make = make_river(empty_cells, cells, river_len)
                if is_make:
                    break

            if not is_make:
                print('Can`t create all rivers')
                break

    def _generate_treasures(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        for _ in range(self.treasure_count):
            if not empty_cells:
                print('Can`t create all treasures')
                break

            idx_cell = random.choice(range(len(empty_cells)))
            treasure_coord = empty_cells[idx_cell]
            make_treasure(cells[treasure_coord[0]][treasure_coord[1]])
            empty_cells.pop(idx_cell)

    def _generate_wormholes(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        wormholes_coord = []
        for _ in range(self.wormholes_count):
            if not empty_cells:
                print('Can`t create all wormholes')
                break

            idx = random.choice(range(len(empty_cells)))
            wormholes_coord.append(empty_cells[idx])
            empty_cells.pop(idx)

        if wormholes_coord:
            make_wormholes(wormholes_coord, cells)

    def _generate_exits(self, cells: List[List[Union[Cell, CellMonolith]]]):
        for _ in range(self.exits_count):
            coord = random.choice(range(1, self.size[0] - 2))
            sides = [(0, coord), (self.size[0] - 1, coord), (coord, 0), (coord, self.size[1] - 1)]
            ex_coord = random.choice(sides)
            make_exit(cells[ex_coord[0]][ex_coord[1]], cells)

    def generate(self) -> StandardLabyrinth:
        cells, empty_cells = self._generate_cells()

        init_y, init_x = self._get_random_coordinates()
        cell = cells[init_y][init_x]

        visited_cells_num = 1
        cells_stack = []
        while visited_cells_num < (self.size[0] - 2) * (self.size[1] - 2):
            neighbors = [curr_cell for curr_cell in get_cell_neighbors(cell, cells) if curr_cell[0].is_isolated]
            if neighbors:
                visited_cells_num += 1
                cells_stack.append(cell)
                curr_neighbor = random.choice(neighbors)
                connect_cells(cell, curr_neighbor)
                cell = curr_neighbor[0]
            else:
                cell = cells_stack.pop()

        self._generate_rivers(cells, empty_cells)
        self._generate_treasures(cells, empty_cells)
        self._generate_wormholes(cells, empty_cells)
        self._generate_exits(cells)

        labyrinth = Labyrinth(cells, empty_cells)
        return labyrinth
