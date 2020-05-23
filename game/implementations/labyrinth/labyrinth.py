from typing import List, Union, Tuple

from game.interfaces.labyrinth.cell import Cell, CellMonolith
from game.interfaces.labyrinth.labyrinth import StandardLabyrinth
from game.interfaces.player import Player
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS
from game.implementations.labyrinth.visualize_constants import sym_player


class Labyrinth(StandardLabyrinth):

    def __init__(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        super().__init__()

        self.cells = cells
        self.empty_cells = empty_cells

    def execute_command(self, command: str, player: Player):
        coordinates = player.get_coordinates
        self.cells[coordinates[0]][coordinates[1]].cell_center = ' '
        new_cell_coordinates = ACTIONS_FUNCTIONS[command](coordinates)

        cell = self.cells[new_cell_coordinates[0]][new_cell_coordinates[1]]
        cell.cell_center = sym_player
        message, new_player_coordinates = cell.execute_command(command, player)

        player.coordinates = new_player_coordinates
        print(message)

    def show_map(self):
        map_str = ''
        for row in range(len(self.cells)):
            row_up = ''
            row_center = ''
            row_down = ''
            for col in range(len(self.cells[0])):
                cell_up, cell_left, cell_center, cell_right, cell_down = self.cells[row][col].show_cell()
                if col == 0:
                    row_up += ' ' + cell_up + ' '
                    row_center += cell_left + cell_center + cell_right
                    row_down += ' ' + cell_down + ' '
                else:
                    row_up += cell_up + ' '
                    row_center += cell_center + cell_right
                    row_down += cell_down + ' '

            if row == 0:
                map_str += row_up + '\n' + row_center + '\n' + row_down + '\n'
            else:
                map_str += row_center + '\n' + row_down + '\n'

        print(map_str)
