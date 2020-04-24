from typing import Tuple


def right(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0], coordinates[1] + 1


def left(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0], coordinates[1] - 1


def up(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0] - 1, coordinates[1]


def down(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates[0] + 1, coordinates[1]


def skip(coordinates: Tuple[int, int]) -> Tuple[int, int]:
    return coordinates
