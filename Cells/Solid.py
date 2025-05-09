from Cell import Cell

class Solid(Cell):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)
