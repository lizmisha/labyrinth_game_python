from typing import Tuple

from game.interfaces.labyrinth.cell import Cell
from game.interfaces.player import Player
from game.implementations.labyrinth.game_actions import GameActionMonolith, GameActionWall
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM, FROM_ACTIONS


class CellBase(Cell):

    def __init__(self, treasure: bool = False):
        self.treasure = treasure
        self.game_actions = dict()

    def execute_command(self, command: str, player: Player) -> Tuple[str, Tuple[int, int]]:
        player_action = ACTIONS_FUNCTIONS[command]
        from_action = ACTIONS2FROM[command]
        return self.game_actions[from_action].execute_action(player, player_action)

    @property
    def is_isolated(self) -> bool:
        isolated = True
        for game_action in self.game_actions.values():
            isolated *= isinstance(game_action, GameActionWall)

        return isolated


def make_monolith_cell(cell: CellBase) -> CellBase:
    for from_action in FROM_ACTIONS:
        cell.game_actions[from_action] = GameActionMonolith()

    return cell


def make_closed_cell(cell: CellBase) -> CellBase:
    for from_action in FROM_ACTIONS:
        cell.game_actions[from_action] = GameActionWall()

    return cell
