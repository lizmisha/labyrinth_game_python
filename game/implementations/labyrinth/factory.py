from game.interfaces.labyrinth.labyrinth import StandardLabyrinth
from game.implementations.labyrinth.constants import BOUND_SIZE, TREASURE_COUNT, EXITS_COUNT, WORMHOLES_COUNT


class LabyrinthFactory:

    def __init__(self, size: int):
        assert BOUND_SIZE[0] <= size <= BOUND_SIZE[1],\
            f'Size should be not less {BOUND_SIZE[0]} and not bigger {BOUND_SIZE[1]}'

        self.size = (size, size)
        self.treasure_count = TREASURE_COUNT
        self.wormholes_count = WORMHOLES_COUNT
        self.exits_count = EXITS_COUNT

    def generate(self) -> StandardLabyrinth: pass
