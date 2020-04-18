from game.interfaces.labyrinth.cell import Cell


class CellEmpty(Cell):

    def __init__(self): pass

    def action(self): pass


class CellTreasure(Cell):

    def __init__(self): pass

    def action(self): pass


class CellWormhole(Cell):

    def __init__(self): pass

    def action(self): pass


class CellWall(Cell):

    def __init__(self): pass

    def action(self): pass


class CellMonolith(Cell):

    def __init__(self): pass

    def action(self): pass


class CellExit(Cell):

    def __init__(self): pass

    def action(self): pass
