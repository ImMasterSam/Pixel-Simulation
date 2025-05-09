from random import choice
from Cells.Solid import Solid

class Sand(Solid):

    color_list = [(235, 235, 0), (255, 255, 0), (205, 205, 0)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 1)  # 1 for sand type
        self.color = choice(self.color_list)