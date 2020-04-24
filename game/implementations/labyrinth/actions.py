from typing import Callable, Tuple

from game.interfaces.labyrinth.action import Action
from game.interfaces.player import Player


def right(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0], coordinates[1] + 1


def left(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0], coordinates[1] - 1


def up(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0] - 1, coordinates[1]


def down(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0] + 1, coordinates[1]


class ActionWall(Action):

    def __init__(self):
        self.message = 'step impossible, wall'

    def execute(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, player.coordinates


class ActionWormhole(Action):

    def __init__(self, coordinates_next: Tuple[int, int]):
        self.coordinates_next = coordinates_next
        self.message = 'step executed, wormhole'

    def execute(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, self.coordinates_next


class ActionTreasure(Action):

    def __init__(self):
        self.message = 'step executed, treasure'

    def execute(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        player.treasure = True
        return self.message, action(player.coordinates)


class ActionMonolith(Action):

    def __init__(self):
        self.message = 'step impossible, monolith'

    def execute(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, player.coordinates


class ActionExecuted(Action):

    def __init__(self):
        self.message = 'step executed'

    def execute(
            self,
            player: Player,
            action: Callable[[Tuple[int, int]], Tuple[int, int]]
    ) -> Tuple[str, Tuple[int, int]]:
        return self.message, action(player.coordinates)
