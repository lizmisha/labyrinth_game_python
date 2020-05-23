from service.interfaces.game import Game
from game.implementations.labyrinth.factory import LabyrinthFactory
from game.implementations.players import PlayerBase


class GameBase(Game):

    def __init__(self):
        self.begin_print = 'Type "start <labyrinth_size>" or "quit"'

    def start(self):
        print(self.begin_print)

        while True:
            command = input().split()

            if not command:
                continue

            if command[0] == 'start' and len(command) > 1:
                size = int(command[1])
                return self.game(size)
            elif command[0] == 'quit':
                return False
            else:
                print('Unknown command')

    def game(self, size: int):
        labyrinth_factory = LabyrinthFactory(size)
        labyrinth = labyrinth_factory.generate()
        player = PlayerBase(labyrinth)
