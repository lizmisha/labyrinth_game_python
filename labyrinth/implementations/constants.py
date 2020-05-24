from game.implementations.player_actions import up, down, right, left, skip


BOUND_SIZE = (4, 10)
BOUND_RIVER_LEN = (3, 4)
RIVER_MAKE_CHANCES = 3

TREASURE_COUNT = 1
WORMHOLES_COUNT = 5
EXITS_COUNT = 1
RIVERS_COUNT = 1

FROM_ACTIONS = {'from down', 'from up', 'from right', 'from left', 'skip'}

ACTIONS2FROM = {
    'go up': 'from down',
    'go down': 'from up',
    'go right': 'from left',
    'go left': 'from right',
    'skip': 'skip'
}

ACTIONS_FROM_REVERSE = {
    'from down': 'from up',
    'from up': 'from down',
    'from left': 'from right',
    'from right': 'from left',
    'skip': 'skip'
}

ACTIONS_FUNCTIONS = {
    'go up': up,
    'go down': down,
    'go right': right,
    'go left': left,
    'skip': skip
}
