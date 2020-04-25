from typing import Dict, List, Tuple

from game.interfaces.labyrinth.cell import Cell
from game.interfaces.labyrinth.game_action import GameAction
from game.implementations.labyrinth.cells import CellBase, CellMonolith
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM, ACTIONS_FROM_REVERSE
from game.implementations.labyrinth.game_actions import (GameActionMonolith, GameActionWall, GameActionExecuted,
                                                         GameActionTreasure, GameActionWormhole)
from game.implementations.labyrinth.constants import FROM_ACTIONS


def make_monolith() -> Dict[str, GameAction]:
    game_actions = dict()
    for from_action in FROM_ACTIONS:
        game_actions[from_action] = GameActionMonolith()

    return game_actions


def make_closed_wall() -> Dict[str, GameAction]:
    game_actions = dict()
    for from_action in FROM_ACTIONS:
        game_actions[from_action] = GameActionWall()

    return game_actions


def get_cell_neighbors(curr_cell: Cell, cells: List[List[Cell]]) -> List[Tuple[CellBase, str]]:
    neighbors = []
    if isinstance(curr_cell, CellMonolith):
        return neighbors

    for action_name in ACTIONS_FUNCTIONS:
        cell_neighbor_coordinates = ACTIONS_FUNCTIONS[action_name](curr_cell.get_coordinates)
        cell_neighbor = cells[cell_neighbor_coordinates[0]][cell_neighbor_coordinates[1]]

        if isinstance(cell_neighbor, CellBase):
            neighbors.append((cell_neighbor, action_name))

    return neighbors


def connect_cells(cell: CellBase, cell_neighbor: Tuple[CellBase, str]):
    from_action = ACTIONS2FROM[cell_neighbor[1]]

    cell_neighbor[0].game_actions[from_action] = GameActionExecuted()
    cell.game_actions[ACTIONS_FROM_REVERSE[from_action]] = GameActionExecuted()


def show_center_cell(center: str, game_action: GameAction) -> str:
    if isinstance(game_action, GameActionTreasure) or isinstance(game_action, GameActionWormhole):
        return game_action.show_command('center')

    return center
