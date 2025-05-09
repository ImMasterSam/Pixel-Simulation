from random import choice
from Cells.Solid import UnmoveableSolid

class Rock(UnmoveableSolid):

    color_list = [(128, 128, 128), (150, 150, 150)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 3)  # 3 for rock type
        self.color = choice(self.color_list)