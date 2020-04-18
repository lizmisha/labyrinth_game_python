from game.implementations.labyrinth.constants import BOUND_SIZE, TREASURE_COUNT, EXITS_COUNT, WORMHOLES_COUNT


class LabyrinthFactory:

    def __init__(self, size: int):
        assert BOUND_SIZE[0] <= size <= BOUND_SIZE[1], 'Size should be not less 4 and not bigger 10'

        self.size = (size, size)
        self.treasure_count = TREASURE_COUNT
        self.wormholes_count = WORMHOLES_COUNT
        self.exits_count = EXITS_COUNT
