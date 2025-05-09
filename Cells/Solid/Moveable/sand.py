from random import choice
from Cells.Solid.moveableSolid import MoveableSolid

class Sand(MoveableSolid):

    color_list = [(235, 235, 0), (255, 255, 0), (205, 205, 0)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 1)  # 1 for sand type
        self.color = choice(self.color_list)

        self.friction = 0.9