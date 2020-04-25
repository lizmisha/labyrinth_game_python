from typing import List

from game.interfaces.labyrinth.cell import Cell
from game.interfaces.labyrinth.labyrinth import StandardLabyrinth
from game.interfaces.player import Player
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS


class Labyrinth(StandardLabyrinth):

    def __init__(self, cells: List[List[Cell]]):
        self.cells = cells

    def execute_command(self, command: str, player: Player):
        coordinates = player.get_coordinates
        new_cell_coordinates = ACTIONS_FUNCTIONS[command](coordinates)

        cell = self.cells[new_cell_coordinates[0]][new_cell_coordinates[1]]
        message, new_player_coordinates = cell.execute_command(command, player)

        player.coordinates = new_player_coordinates
        print(message)
