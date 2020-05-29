from labyrinth.implementations.labyrinth import Labyrinth, LabyrinthWithBear


LABYRINTHS_COLLECTIONS = {
    'standard': Labyrinth,
    'with bear': LabyrinthWithBear
}


def get_labyrinth(labyrinth_type: str):
    return LABYRINTHS_COLLECTIONS.get(labyrinth_type, None)
