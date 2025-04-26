import pygame
from Cell import Cell

class Rock(Cell):

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 3)  # 1 for sand type

    def update(self):
        pass

    def render(self, screen, cell_width: int, cell_height: int):
        pygame.draw.rect(screen, (128, 128, 128), (self.col * cell_width, self.row * cell_height, cell_width, cell_height))