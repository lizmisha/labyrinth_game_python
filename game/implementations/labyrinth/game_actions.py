from typing import Callable, Tuple

from game.interfaces.labyrinth.game_action import GameAction
from game.interfaces.player import Player


class GameActionWall(GameAction):

    def __init__(self):
        self.message = 'step impossible, wall'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, player.get_coordinates


class GameActionWormhole(GameAction):

    def __init__(self, coordinates_next: Tuple[int, int]):
        self.coordinates_next = coordinates_next
        self.message = 'step executed, wormhole'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, self.coordinates_next


class GameActionTreasure(GameAction):

    def __init__(self):
        self.message = 'step executed, treasure'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        player.treasure = True
        return self.message, action(player.get_coordinates)


class GameActionMonolith(GameAction):

    def __init__(self):
        self.message = 'step impossible, monolith'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, player.get_coordinates


class GameActionExecuted(GameAction):

    def __init__(self):
        self.message = 'step executed'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, action(player.get_coordinates)


class GameActionNothing(GameAction):

    def __init__(self):
        self.message = 'step executed'

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, action(player.get_coordinates)


class GameActionExit(GameAction):

    def __init__(self):
        self.funny_message = 'congratulations, you passed the game!'
        self.sad_message = 'you can`t exit, because you haven`t treasure :('

    def execute_action(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        if player.have_treasure:
            return self.funny_message, player.get_coordinates

        return self.sad_message, player.get_coordinates
