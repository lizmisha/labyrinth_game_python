from typing import Callable, Tuple

from game.interfaces.labyrinth.game_action import GameAction
from game.interfaces.player import Player


class GameActionWall(GameAction):

    def __init__(self):
        self.message = 'step impossible, wall'
        self.show = {
            'up': '_',
            'left': '|',
            'right': '|',
            'down': '\u25AC',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        return self.message, player.get_coordinates, False

    def show_command(self, command: str) -> str:
        return self.show[command]


class GameActionWormhole(GameAction):

    def __init__(self, coordinates_next: Tuple[int, int]):
        self.coordinates_next = coordinates_next
        self.message = 'step executed, wormhole'
        self.show = {
            'up': ' ',
            'left': ' ',
            'right': ' ',
            'down': ' ',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        return self.message, self.coordinates_next, False

    def show_command(self, command: str) -> str:
        return self.show[command]


class GameActionTreasure(GameAction):

    def __init__(self):
        self.message = 'step executed, treasure'
        self.show = {
            'up': ' ',
            'left': ' ',
            'right': ' ',
            'down': ' ',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        player.treasure = True
        return self.message, action(player.get_coordinates), False

    def show_command(self, command: str) -> str:
        return self.show[command]


class GameActionMonolith(GameAction):

    def __init__(self):
        self.message = 'step impossible, monolith'
        self.show = {
            'up': '_',
            'left': '|',
            'right': '|',
            'down': '\u25AC',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        return self.message, player.get_coordinates, False

    def show_command(self, command: str) -> str:
        return self.show[command]


class GameActionExecuted(GameAction):

    def __init__(self):
        self.message = 'step executed'
        self.show = {
            'up': ' ',
            'left': ' ',
            'right': ' ',
            'down': ' ',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        return self.message, action(player.get_coordinates), False

    def show_command(self, command: str) -> str:
        return self.show[command]


class GameActionRiver(GameAction):

    def __init__(self, coordinates_next: Tuple[int, int]):
        self.message = 'step executed, river'
        self.coordinates_next = coordinates_next
        self.show = {
            'up': ' ',
            'left': ' ',
            'right': ' ',
            'down': ' ',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        return self.message, self.coordinates_next, False

    def show_command(self, command: str) -> str:
        return self.show[command]


class GameActionNothing(GameAction):

    def __init__(self):
        self.message = 'step executed'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        return self.message, action(player.get_coordinates), False

    def show_command(self, command: str) -> str:
        return ' '


class GameActionExit(GameAction):

    def __init__(self):
        self.funny_message = 'congratulations, you passed the game!'
        self.sad_message = 'you can`t exit, because you haven`t treasure :('
        self.show = {
            'up': ' ',
            'left': ' ',
            'right': ' ',
            'down': ' ',
        }

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int], bool]:
        if player.have_treasure:
            return self.funny_message, player.get_coordinates, True

        return self.sad_message, player.get_coordinates, False

    def show_command(self, command: str) -> str:
        return self.show[command]
