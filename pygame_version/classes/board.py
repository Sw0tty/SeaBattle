"""
"""


class Cell:
    def __init__(self, x_size: int, y_size: int, position: tuple, cell_object: object):
        self.x_size = x_size
        self.y_size = y_size
        self.position = position
        self.cell_object = cell_object
        self.color = None


class Board:

    def __init__(self):
        self.cells = []


class FieldGrid:
    pass


class FieldsPrinter:
    pass
