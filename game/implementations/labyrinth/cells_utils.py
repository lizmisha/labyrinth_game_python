from typing import Dict, List, Tuple, Union

from game.interfaces.labyrinth.cell import Cell, CellMonolith
from game.interfaces.labyrinth.game_action import GameAction
from game.implementations.labyrinth.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM, ACTIONS_FROM_REVERSE, FROM_ACTIONS
from game.implementations.labyrinth.visualize_constants import sym_treasure, sym_wormhole
from game.implementations.labyrinth.game_actions import (GameActionMonolith, GameActionWall, GameActionTreasure,
                                                         GameActionExecuted, GameActionExit, GameActionWormhole)


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


def make_treasure(curr_cell: Cell):
    curr_cell.cell_center = sym_treasure
    for action in FROM_ACTIONS:
        if isinstance(curr_cell.game_actions[action], GameActionExecuted):
            curr_cell.game_actions[action] = GameActionTreasure()


def make_wormholes(coords: List[Tuple[int, int]], cells: List[List[Union[Cell, CellMonolith]]]):
    for i, curr_coord in enumerate(coords):
        next_idx = (i + 1) % len(coords)
        next_coord = coords[next_idx]

        curr_cell = cells[curr_coord[0]][curr_coord[1]]
        curr_cell.cell_center = sym_wormhole
        for action in FROM_ACTIONS:
            if isinstance(curr_cell.game_actions[action], GameActionExecuted):
                curr_cell.game_actions[action] = GameActionWormhole(next_coord)


def make_exit(curr_cell: CellMonolith, cells: List[List[Union[Cell, CellMonolith]]]):
    curr_cell.cell_center = ' '
    neighbors = get_cell_neighbors(curr_cell, cells)
    for curr_neighbor in neighbors:
        cell_neighbor, neighbor_action = curr_neighbor
        neighbor_action = ACTIONS2FROM[neighbor_action]
        neighbor_action = ACTIONS_FROM_REVERSE[neighbor_action]
        curr_cell.game_actions[neighbor_action] = GameActionExit()

        neighbor_action = ACTIONS_FROM_REVERSE[neighbor_action]
        cell_neighbor.game_actions[neighbor_action] = GameActionExit()
        curr_cell.game_actions[neighbor_action] = GameActionExit()


def is_correct_coordinate(coord: Tuple[int, int], size: Tuple[int, int]) -> bool:
    flag = False
    if (coord[0] < size[0]) and (coord[0] >= 0) and (coord[1] < size[1]) and (coord[1] >= 1):
        flag = True
    return flag


def get_cell_neighbors(
        curr_cell: Union[Cell, CellMonolith],
        cells: List[List[Union[Cell, CellMonolith]]]
) -> List[Tuple[Cell, str]]:
    neighbors = []
    for action_name in ACTIONS_FUNCTIONS:
        cell_neighbor_coordinates = ACTIONS_FUNCTIONS[action_name](curr_cell.get_coordinates)
        if not is_correct_coordinate(cell_neighbor_coordinates, (len(cells), len(cells[0]))):
            continue

        cell_neighbor = cells[cell_neighbor_coordinates[0]][cell_neighbor_coordinates[1]]

        if isinstance(cell_neighbor, Cell):
            neighbors.append((cell_neighbor, action_name))

    return neighbors


def connect_cells(cell: Union[Cell, CellMonolith], cell_neighbor: Tuple[Cell, str]):
    from_action = ACTIONS2FROM[cell_neighbor[1]]

    cell_neighbor[0].game_actions[from_action] = GameActionExecuted()
    cell.game_actions[ACTIONS_FROM_REVERSE[from_action]] = GameActionExecuted()
