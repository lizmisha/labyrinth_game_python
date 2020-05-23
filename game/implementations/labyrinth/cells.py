from typing import Tuple

from game.interfaces.labyrinth.cell import Cell, CellMonolith
from game.interfaces.player import Player
from game.implementations.labyrinth.game_actions import GameActionWall, GameActionMonolith
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM
from game.implementations.labyrinth.cells_utils import make_closed_wall, make_monolith
from game.implementations.labyrinth.visualize_constants import sym_monolith


class CellBase(Cell):

    def __init__(self, coordinates: Tuple[int, int], treasure: bool = False):
        super().__init__()

        self.coordinates = coordinates
        self.treasure = treasure
        self.game_actions = make_closed_wall()

        self.cell_center = ' '

    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]:
        player_action = ACTIONS_FUNCTIONS[command]
        from_action = ACTIONS2FROM[command]
        return self.game_actions[from_action].execute_action(player, player_action)

    @property
    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates

    @property
    def is_isolated(self) -> bool:
        isolated = True
        for game_action in self.game_actions.values():
            isolated *= (isinstance(game_action, GameActionWall) or isinstance(game_action, GameActionMonolith))

        return isolated

    def show_cell(self) -> Tuple[str, str, str, str, str]:
        up = self.game_actions['from up'].show_command('up')
        down = self.game_actions['from down'].show_command('down')
        right = self.game_actions['from right'].show_command('right')
        left = self.game_actions['from left'].show_command('left')
        return up, left, self.cell_center, right, down


class CellMonolithBase(CellMonolith):

    def __init__(self, coordinates: Tuple[int, int]):
        super().__init__()

        self.coordinates = coordinates
        self.game_actions = make_monolith()
        self.cell_center = sym_monolith

    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]:
        player_action = ACTIONS_FUNCTIONS[command]
        from_action = ACTIONS2FROM[command]
        return self.game_actions[from_action].execute_action(player, player_action)

    @property
    def get_coordinates(self) -> Tuple[int, int]:
        return self.coordinates

    def show_cell(self) -> Tuple[str, str, str, str, str]:
        up = self.game_actions['from up'].show_command('up')
        down = self.game_actions['from down'].show_command('down')
        right = self.game_actions['from right'].show_command('right')
        left = self.game_actions['from left'].show_command('left')
        return up, left, self.cell_center, right, down
