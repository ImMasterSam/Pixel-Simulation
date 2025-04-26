import pygame
from Cell import Cell

class Water(Cell):

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 2)  # 2 for sand type

    def update(self):

        movement = ((0, 1), (-1, 1), (1, 1), (-1, 0), (1, 0))

        for move in movement:
            next_row = self.row + move[1]
            next_col = self.col + move[0]

            next_type = self.grid.getCellType(next_row, next_col)
            if next_type == 0:
                self.grid.swapCell(self.row, self.col, next_row, next_col)
                return

    def render(self, screen, cell_width: int, cell_height: int):
        pygame.draw.rect(screen, (0, 0, 255), (self.col * cell_width, self.row * cell_height, cell_width, cell_height))