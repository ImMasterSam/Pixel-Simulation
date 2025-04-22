import pygame

class Cell:

    def __init__(self, grid, row: int, col: int, type: int = 0):
        self.grid = grid
        self.row = row
        self.col = col
        self.type = type

    def update(self):

        offsets = [0, -1, 1] 

        if self.type == 1:  # Sand
            for offset in offsets:
                next_row = self.row + 1
                next_col = self.col + offset

                next_type = self.grid.getCellType(next_row, next_col)
                if next_type == 0:
                    self.grid.swapCell(self.row, self.col, next_row, next_col)
    
    def render(self, screen, cell_width: int, cell_height: int):
        if self.type != 0:
            pygame.draw.rect(screen, (255, 255, 0), (self.col * cell_width, self.row * cell_height, cell_width, cell_height))