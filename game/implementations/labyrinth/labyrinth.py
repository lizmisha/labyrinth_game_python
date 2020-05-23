from typing import List, Union, Tuple

from game.interfaces.labyrinth.cell import Cell, CellMonolith
from game.interfaces.labyrinth.labyrinth import StandardLabyrinth
from game.interfaces.player import Player
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS


class Labyrinth(StandardLabyrinth):

    def __init__(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        self.cells = cells
        self.empty_cells = empty_cells
        self.previous_center_cell = ' '

    def execute_command(self, command: str, player: Player) -> Tuple[bool, str]:
        coordinates = player.get_coordinates
        self.cells[coordinates[0]][coordinates[1]].cell_center = self.previous_center_cell

        new_cell_coordinates = ACTIONS_FUNCTIONS[command](coordinates)

        cell = self.cells[new_cell_coordinates[0]][new_cell_coordinates[1]]
        message, new_player_coordinates, is_end = cell.execute_command(command, player)

        cell = self.cells[new_player_coordinates[0]][new_player_coordinates[1]]
        self.previous_center_cell = cell.cell_center
        cell.cell_center = player.icon

        player.coordinates = new_player_coordinates

        return is_end, message

    @property
    def get_empty_cells(self) -> List[Tuple[int, int]]:
        return self.empty_cells

    def put_player_icon(self, icon: str, coordinates: Tuple[int, int]):
        self.cells[coordinates[0]][coordinates[1]].cell_center = icon

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
