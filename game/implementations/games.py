import os
import pickle
import random
from typing import Tuple

from game.interfaces.game import Game
from game.implementations.players import PlayerBase, BearBase
from labyrinth.implementations.constants import (ACTIONS_FUNCTIONS, BOUND_RIVER_LEN, RIVERS_COUNT, TREASURE_COUNT,
                                                 WORMHOLES_COUNT, EXITS_COUNT)
from labyrinth.implementations.factory import LabyrinthFactory


class GameBase(Game):

    def __init__(
            self,
            labyrinth_type: str = 'standard',
            rivers_count: int = RIVERS_COUNT,
            rivers_bound: Tuple[int, int] = BOUND_RIVER_LEN,
            treasure_count: int = TREASURE_COUNT,
            wormholes_count: int = WORMHOLES_COUNT,
            exits_count: int = EXITS_COUNT
    ):
        self.labyrinth_type = labyrinth_type
        self.rivers_count = rivers_count
        self.rivers_bound = rivers_bound
        self.treasure_count = treasure_count
        self.wormholes_count = wormholes_count
        self.exits_count = exits_count

        self.begin_print = 'Type "start <labyrinth_size>", "save <filename>" or "quit"'
        self.labyrinth = None
        self.player = None

    def _make_game(self, size: int):
        labyrinth_factory = LabyrinthFactory(
            size=size,
            labyrinth_type=self.labyrinth_type,
            rivers_count=self.rivers_count,
            rivers_bound=self.rivers_bound,
            treasure_count=self.treasure_count,
            wormholes_count=self.wormholes_count,
            exits_count=self.exits_count
        )
        self.labyrinth = labyrinth_factory.generate()

        if len(self.labyrinth.get_empty_cells) == 0:
            raise IndexError('Can`t create game')

        idx_coord = random.choice(range(len(self.labyrinth.get_empty_cells)))
        player_coord = self.labyrinth.get_empty_cells[idx_coord]
        self.labyrinth.pop_empty_cell(idx_coord)
        self.player = PlayerBase(player_coord)
        self.labyrinth.put_player_icon(self.player.icon, player_coord)

    def start(self):
        while True:
            print(self.begin_print)
            command = input().split()

            if not command:
                continue

            if command[0] == 'start' and len(command) == 2:
                size = int(command[1])
                self._make_game(size)
                self.game()
                break
            elif command[0] == 'quit':
                break
            elif command[0] == 'load' and len(command) == 2:
                try:
                    with open(os.path.join('saves', command[1] + '.pkl'), 'rb') as f:
                        loaded_game = pickle.load(f)
                    print('Game loaded.')
                    loaded_game.game()
                    break
                except FileNotFoundError:
                    print('No saved game with this name')
            else:
                print('Unknown command')

    def save(self, filename: str):
        os.makedirs('saves', exist_ok=True)
        with open(os.path.join('saves', filename) + '.pkl', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

        print(f'Game has been saved.')

    def game(self):
        while True:
            command = input().split()
            if command[0] == 'save' and len(command) == 2:
                self.save(command[1])
                continue

            command = ' '.join(command)
            if command == 'quit':
                break

            if command == 'map':
                self.labyrinth.show_map()
            else:
                try:
                    is_end, message = self.labyrinth.execute_command(command, self.player)
                    print(message)
                    if is_end:
                        break
                except KeyError as err:
                    print(err)


class GameBear(GameBase):

    def __init__(
            self,
            labyrinth_type: str = 'with bear',
            rivers_count: int = RIVERS_COUNT,
            rivers_bound: Tuple[int, int] = BOUND_RIVER_LEN,
            treasure_count: int = TREASURE_COUNT,
            wormholes_count: int = WORMHOLES_COUNT,
            exits_count: int = EXITS_COUNT
    ):
        super().__init__(labyrinth_type, rivers_count, rivers_bound, treasure_count, wormholes_count, exits_count)
        self.bear = None

    def _make_game(self, size: int):
        super()._make_game(size)

        bear_coord = random.choice(self.labyrinth.get_empty_cells)
        self.bear = BearBase(bear_coord)
        self.labyrinth.put_player_icon(self.bear.icon, bear_coord)

    def game(self):
        while True:
            command = input().split()
            if command[0] == 'save' and len(command) == 2:
                self.save(command[1])
                continue

            command = ' '.join(command)
            if command == 'quit':
                break

            if command == 'map':
                self.labyrinth.show_map()
            elif command in ACTIONS_FUNCTIONS:
                _, _ = self.labyrinth.execute_command(random.choice(list(ACTIONS_FUNCTIONS)), self.bear)
                is_end, message = self.labyrinth.execute_command(command, self.player)
                print(message)
                if is_end:
                    break
            else:
                print('Unknown command')
