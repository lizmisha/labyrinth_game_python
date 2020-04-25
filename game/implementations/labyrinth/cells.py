from typing import Tuple

from game.interfaces.labyrinth.cell import Cell
from game.interfaces.player import Player
from game.implementations.labyrinth.game_actions import GameActionWall
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM
from game.implementations.labyrinth.cells_utils import make_closed_wall, make_monolith, show_center_cell


class CellBase(Cell):

    def __init__(self, coordinates: Tuple[int, int], treasure: bool = False):
        self.coordinates = coordinates
        self.treasure = treasure
        self.game_actions = make_closed_wall()

    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]:
        player_action = ACTIONS_FUNCTIONS[command]
        from_action = ACTIONS2FROM[command]
        return self.game_actions[from_action].execute_action(player, player_action)

    @property
    def get_coordinates(self):
        return self.coordinates

    @property
    def is_isolated(self) -> bool:
        isolated = True
        for game_action in self.game_actions.values():
            isolated *= isinstance(game_action, GameActionWall)

        return isolated

    def show_cell(self) -> Tuple[str, str, str]:
        up = self.game_actions['from up'].show_command('up')
        down = self.game_actions['from down'].show_command('down')

        curr_center = ' '
        curr_center = show_center_cell(curr_center, self.game_actions['from right'])
        curr_center = show_center_cell(curr_center, self.game_actions['from left'])

        right = self.game_actions['from right'].show_command('right')
        left = self.game_actions['from left'].show_command('left')
        center = right + curr_center + left

        return up, center, down


class CellMonolith(Cell):

    def __init__(self, coordinates: Tuple[int, int]):
        self.coordinates = coordinates
        self.game_actions = make_monolith()

    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]:
        player_action = ACTIONS_FUNCTIONS[command]
        from_action = ACTIONS2FROM[command]
        return self.game_actions[from_action].execute_action(player, player_action)

    @property
    def get_coordinates(self):
        return self.coordinates

    def show_cell(self) -> Tuple[str, str, str]:
        up = self.game_actions['from up'].show_command('up')
        down = self.game_actions['from down'].show_command('down')

        right = self.game_actions['from right'].show_command('right')
        left = self.game_actions['from left'].show_command('left')
        center = right + ' ' + left

        return up, center, down
