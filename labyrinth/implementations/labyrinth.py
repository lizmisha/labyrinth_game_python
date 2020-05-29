import random
from typing import List, Union, Tuple

from game.interfaces.player import Player, Bear
from labyrinth.interfaces.cell import Cell, CellMonolith
from labyrinth.interfaces.labyrinth import StandardLabyrinth
from labyrinth.implementations.cells_utils import get_cell_neighbors
from labyrinth.implementations.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM, BEAR_DAMAGE_MESSAGE, BEAR_KILL_MESSAGE
from labyrinth.implementations.game_actions import GameActionWall
from labyrinth.implementations.visualize_constants import SYM_BEAR, SYM_PLAYER


class Labyrinth(StandardLabyrinth):

    def __init__(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        self.cells = cells
        self.empty_cells = empty_cells
        self.previous_center_cell = ' '

    def execute_command(self, command: str, player: Player) -> Tuple[bool, str]:
        if command not in ACTIONS_FUNCTIONS:
            raise KeyError('Unknown command')

        old_cell_coordinates = player.get_coordinates
        self.cells[old_cell_coordinates[0]][old_cell_coordinates[1]].cell_center = self.previous_center_cell

        new_cell_coordinates = ACTIONS_FUNCTIONS[command](old_cell_coordinates)

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

    def pop_empty_cell(self, idx: int):
        _ = self.empty_cells.pop(idx)

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


class LabyrinthWithBear(Labyrinth):

    def __init__(self, cells: List[List[Union[Cell, CellMonolith]]], empty_cells: List[Tuple[int, int]]):
        super().__init__(cells, empty_cells)
        self.previous_center_cell_bear = ' '

    def execute_command(self, command: str, player: Union[Player, Bear]) -> Tuple[bool, str]:
        old_cell_coordinates = player.get_coordinates
        old_cell = self.cells[old_cell_coordinates[0]][old_cell_coordinates[1]]
        if old_cell.cell_center == player.icon:
            if isinstance(player, Bear):
                old_cell.cell_center = self.previous_center_cell_bear
            else:
                old_cell.cell_center = self.previous_center_cell

        new_cell_coordinates = ACTIONS_FUNCTIONS[command](old_cell_coordinates)
        cell = self.cells[new_cell_coordinates[0]][new_cell_coordinates[1]]
        message, new_player_coordinates, is_end = cell.execute_command(command, player)
        cell = self.cells[new_player_coordinates[0]][new_player_coordinates[1]]
        player.coordinates = new_player_coordinates

        if cell.cell_center == SYM_BEAR and not isinstance(player, Bear):
            player.damage()

            curr_neighbors = get_cell_neighbors(cell, self.cells)
            neighbors = []
            for neighbor in curr_neighbors:
                cell, command, _ = neighbor
                from_action = ACTIONS2FROM[command]
                if not isinstance(cell.game_actions[from_action], GameActionWall):
                    neighbors.append(neighbor)

            if player.health == 0 or len(neighbors) == 0:
                return True, BEAR_KILL_MESSAGE

            cell, command, _ = random.choice(neighbors)
            curr_message, new_player_coordinates, is_end = cell.execute_command(command, player)
            message = BEAR_DAMAGE_MESSAGE + '\n' + curr_message
            cell = self.cells[new_player_coordinates[0]][new_player_coordinates[1]]
            player.coordinates = new_player_coordinates

        if isinstance(player, Bear):
            if cell.cell_center != SYM_PLAYER:
                self.previous_center_cell_bear = cell.cell_center
            else:
                self.previous_center_cell_bear = self.previous_center_cell
        else:
            self.previous_center_cell = cell.cell_center

        cell.cell_center = player.icon
        return is_end, message
