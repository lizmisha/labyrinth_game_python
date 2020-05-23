import random

from service.interfaces.game import Game
from game.implementations.labyrinth.factory import LabyrinthFactory
from game.implementations.players import PlayerBase


class GameBase(Game):

    def __init__(self):
        self.begin_print = 'Type "start <labyrinth_size>" or "quit"'
        self.labyrinth = None
        self.player = None

    def _make_game(self, size: int):
        labyrinth_factory = LabyrinthFactory(size)
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
                is_end, message = self.labyrinth.execute_command(command, self.player)
                print(message)
                if is_end:
                    break
