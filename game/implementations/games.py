import random
from typing import Tuple

from game.interfaces.game import Game
from game.implementations.players import PlayerBase
from labyrinth.implementations.constants import (BOUND_RIVER_LEN, RIVERS_COUNT, TREASURE_COUNT, WORMHOLES_COUNT,
                                                 EXITS_COUNT)
from labyrinth.implementations.factory import LabyrinthFactory


class GameBase(Game):

    def __init__(
            self,
            rivers_count: int = RIVERS_COUNT,
            rivers_bound: Tuple[int, int] = BOUND_RIVER_LEN,
            treasure_count: int = TREASURE_COUNT,
            wormholes_count: int = WORMHOLES_COUNT,
            exits_count: int = EXITS_COUNT
    ):
        self.rivers_count = rivers_count
        self.rivers_bound = rivers_bound
        self.treasure_count = treasure_count
        self.wormholes_count = wormholes_count
        self.exits_count = exits_count

        self.begin_print = 'Type "start <labyrinth_size>" or "quit"'
        self.labyrinth = None
        self.player = None

    def _make_game(self, size: int):
        labyrinth_factory = LabyrinthFactory(
            size=size,
            rivers_count=self.rivers_count,
            rivers_bound=self.rivers_bound,
            treasure_count=self.treasure_count,
            wormholes_count=self.wormholes_count,
            exits_count=self.exits_count
        )
        self.labyrinth = labyrinth_factory.generate()

        player_coord = random.choice(self.labyrinth.get_empty_cells)
        self.player = PlayerBase(player_coord)
        self.labyrinth.put_player_icon(self.player.icon, player_coord)

    def start(self):
        print(self.begin_print)

        while True:
            command = input().split()

            if not command:
                continue

            if command[0] == 'start' and len(command) > 1:
                size = int(command[1])
                self._make_game(size)
                self.game()
                break
            elif command[0] == 'quit':
                break
            else:
                print('Unknown command')

    def game(self):
        while True:
            command = ' '.join(input().split())
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
