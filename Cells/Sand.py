import pygame
from random import choice
from Cell import Cell

class Sand(Cell):

    color_list = [(235, 235, 0), (255, 255, 0), (205, 205, 0)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 1)  # 1 for sand type
        self.color = choice(self.color_list)

    def update(self):
        offsets = [0, -1, 1] 

        for offset in offsets:
            next_row = self.row + 1
            next_col = self.col + offset

            next_type = self.grid.getCellType(next_row, next_col)
            if next_type == 0 or next_type == 2: 
                self.grid.swapCell(self.row, self.col, next_row, next_col)
                break 

    def render(self, screen, cell_width: int, cell_height: int):
        pygame.draw.rect(screen, self.color, (self.col * cell_width, self.row * cell_height, cell_width, cell_height))