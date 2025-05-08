import pygame
from random import choice
from Cell import Cell

class Rock(Cell):

    color_list = [(128, 128, 128), (150, 150, 150)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 3)  # 3 for rock type
        self.color = choice(self.color_list)

    def update(self):
        pass