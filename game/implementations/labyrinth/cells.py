from game.interfaces.labyrinth.cell import Cell


class CellEmpty(Cell):

    def __init__(self): pass

    def action(self): pass


class CellTreasure(Cell):

    def __init__(self): pass

    def action(self): pass


class CellFinish(Cell):

    def __init__(self): pass

    def action(self): pass
