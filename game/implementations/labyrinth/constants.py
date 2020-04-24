from game.implementations.labyrinth.actions import up, down, right, left


BOUND_SIZE = (4, 10)

TREASURE_COUNT = 1
WORMHOLES_COUNT = 5
EXITS_COUNT = 1

ACTIONS_FROM = {
    'go up': 'from down',
    'go down': 'from up',
    'go right': 'from left',
    'go left': 'from right'
}

ACTIONS_FUNCTIONS = {
    'go up': up,
    'go down': down,
    'go right': right,
    'go left': left
}
