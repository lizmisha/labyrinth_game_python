from typing import Tuple

from game.interfaces.labyrinth.cell import Cell
from game.interfaces.player import Player
from game.implementations.labyrinth.game_actions import GameActionWall
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM
from game.implementations.labyrinth.cells_utils import make_closed_wall, make_monolith


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
