from game.interfaces.labyrinth.labyrinth import StandardLabyrinth


class Labyrinth(StandardLabyrinth):

    def __init__(self, cells):
        self.cells = cells

    def execute_action(self): pass
