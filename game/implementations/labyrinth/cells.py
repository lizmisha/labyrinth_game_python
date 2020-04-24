from typing import Tuple

from game.interfaces.labyrinth.cell import Cell


class CellBase(Cell):

    def __init__(self, treasure: bool): pass

    def action(self, command: str) -> Tuple[str, Tuple[int, int]]: pass


class CellExit(Cell):

    def __init__(self): pass

    def action(self, command: str) -> Tuple[str, Tuple[int, int]]: pass
