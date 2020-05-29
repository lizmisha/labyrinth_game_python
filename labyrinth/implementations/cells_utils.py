import random
from typing import Dict, List, Tuple, Union, Set

from labyrinth.interfaces.cell import Cell, CellMonolith
from labyrinth.interfaces.game_action import GameAction
from labyrinth.implementations.constants import ACTIONS_FUNCTIONS, ACTIONS2FROM, ACTIONS_FROM_REVERSE, FROM_ACTIONS
from labyrinth.implementations.visualize_constants import SYM_TREASURE, SYM_WORMHOLE, SYM_RIVER
from labyrinth.implementations.game_actions import (GameActionMonolith, GameActionWall, GameActionTreasure,
                                                    GameActionExecuted, GameActionExit, GameActionWormhole,
                                                    GameActionRiver)


def make_monolith() -> Dict[str, GameAction]:
    game_actions = dict()
    for from_action in FROM_ACTIONS:
        game_actions[from_action] = GameActionMonolith()

    return game_actions


def make_closed_wall() -> Dict[str, GameAction]:
    game_actions = dict()
    for from_action in FROM_ACTIONS:
        if from_action == 'skip':
            game_actions[from_action] = GameActionExecuted()
        else:
            game_actions[from_action] = GameActionWall()

    return game_actions


def choose_river_cell(
        curr_cell: Cell,
        cells: List[List[Union[Cell, CellMonolith]]],
        neighbors_coord: Set[Tuple[int, int]]
) -> Tuple[Union[Tuple[int, int], None], Set[Tuple[int, int]]]:
    neighbors_candidate = get_cell_neighbors(curr_cell, cells)
    neighbors = []
    for neighbor_data in neighbors_candidate:
        neighbor_cell, action, neighbor_coord = neighbor_data
        action = ACTIONS2FROM[action]
        if neighbor_coord not in neighbors_coord and not isinstance(neighbor_cell.game_actions[action], GameActionWall):
            neighbors.append(neighbor_coord)

    if len(neighbors) == 0:
        return None, neighbors_coord

    river_idx = random.choice(range(len(neighbors)))
    river_coord = neighbors[river_idx]
    neighbors_coord.add(river_coord)

    return river_coord, neighbors_coord


def make_rivers_cells(rivers_coords: List[Tuple[int, int]], cells: List[List[Union[Cell, CellMonolith]]]):
    for idx in range(len(rivers_coords)):
        curr_coord = rivers_coords[idx]
        curr_cell = cells[curr_coord[0]][curr_coord[1]]
        curr_cell.cell_center = SYM_RIVER
        if idx + 2 < len(rivers_coords):
            next_coord = rivers_coords[idx + 2]
        else:
            next_coord = rivers_coords[len(rivers_coords) - 1]

        for action in FROM_ACTIONS:
            if isinstance(curr_cell.game_actions[action], GameActionExecuted):
                curr_cell.game_actions[action] = GameActionRiver(next_coord)


def make_river(
        empty_coords: List[Tuple[int, int]],
        cells: List[List[Union[Cell, CellMonolith]]],
        river_len: int
) -> bool:
    idx_river = random.choice(range(len(empty_coords)))
    coord_river = empty_coords[idx_river]
    curr_cell = cells[coord_river[0]][coord_river[1]]

    river_neighbors = set()
    river_neighbors.add(coord_river)
    river_coords = [coord_river]
    for _ in range(river_len - 1):
        curr_coord, river_neighbors = choose_river_cell(curr_cell, cells, river_neighbors)
        if curr_coord is None:
            break

        river_coords.append(curr_coord)
        curr_cell = cells[curr_coord[0]][curr_coord[1]]

    if len(river_coords) < river_len:
        curr_coord = river_coords[0]
        curr_cell = cells[curr_coord[0]][curr_coord[1]]
        curr_len = len(river_coords)
        for _ in range(river_len - curr_len):
            curr_coord, river_neighbors = choose_river_cell(curr_cell, cells, river_neighbors)
            if curr_coord is None:
                break

            river_coords.insert(0, curr_coord)
            curr_cell = cells[curr_coord[0]][curr_coord[1]]

    if len(river_coords) < river_len:
        return False

    for curr_coord in river_coords:
        empty_coords.remove(curr_coord)

    make_rivers_cells(river_coords, cells)
    return True


def make_treasure(curr_cell: Cell):
    curr_cell.cell_center = SYM_TREASURE
    for action in FROM_ACTIONS:
        if isinstance(curr_cell.game_actions[action], GameActionExecuted):
            curr_cell.game_actions[action] = GameActionTreasure()


def make_wormholes(coords: List[Tuple[int, int]], cells: List[List[Union[Cell, CellMonolith]]]):
    for i, curr_coord in enumerate(coords):
        next_idx = (i + 1) % len(coords)
        next_coord = coords[next_idx]

        curr_cell = cells[curr_coord[0]][curr_coord[1]]
        curr_cell.cell_center = SYM_WORMHOLE
        for action in FROM_ACTIONS:
            if isinstance(curr_cell.game_actions[action], GameActionExecuted):
                curr_cell.game_actions[action] = GameActionWormhole(next_coord)


def make_exit(curr_cell: CellMonolith, cells: List[List[Union[Cell, CellMonolith]]]):
    curr_cell.cell_center = ' '
    neighbors = get_cell_neighbors(curr_cell, cells)
    for curr_neighbor in neighbors:
        cell_neighbor, neighbor_action, _ = curr_neighbor
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
) -> List[Tuple[Cell, str, Tuple[int, int]]]:
    neighbors = []
    for action_name in ACTIONS_FUNCTIONS:
        if action_name == 'skip':
            continue

        cell_neighbor_coordinates = ACTIONS_FUNCTIONS[action_name](curr_cell.get_coordinates)
        if not is_correct_coordinate(cell_neighbor_coordinates, (len(cells), len(cells[0]))):
            continue

        cell_neighbor = cells[cell_neighbor_coordinates[0]][cell_neighbor_coordinates[1]]

        if isinstance(cell_neighbor, Cell):
            neighbors.append((cell_neighbor, action_name, cell_neighbor_coordinates))

    return neighbors


def connect_cells(cell: Union[Cell, CellMonolith], cell_neighbor: Tuple[Cell, str]):
    from_action = ACTIONS2FROM[cell_neighbor[1]]

    cell_neighbor[0].game_actions[from_action] = GameActionExecuted()
    cell.game_actions[ACTIONS_FROM_REVERSE[from_action]] = GameActionExecuted()
