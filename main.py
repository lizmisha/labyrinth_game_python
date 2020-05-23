from game.implementations.labyrinth.factory import LabyrinthFactory


if __name__ == '__main__':
    labyrinth_factory = LabyrinthFactory(10)
    labyrinth = labyrinth_factory.generate()
    labyrinth.show_map()
