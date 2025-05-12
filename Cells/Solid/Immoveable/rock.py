from random import choice
from Cells.Solid.immoveableSolid import ImmoveableSolid

class Rock(ImmoveableSolid):

    color_list = [(128, 128, 128), (150, 150, 150)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 3)  # 3 for rock type
        self.color = choice(self.color_list)