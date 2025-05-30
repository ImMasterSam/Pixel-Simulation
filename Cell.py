import pygame

class Cell:

    gravity = 0.1

    def __init__(self, grid, row: int, col: int, type: int = 0):
        self.grid = grid
        self.row = row
        self.col = col
        self.color = (0, 0, 0)
        self.type = type
        self.updated = False

        self.density = 0
        self.isFreeFalling = False

    def update(self):
        '''Override this method in subclasses to define the behavior of the cell'''
        self.updated = True
        pass
    
    def render(self, screen, cell_width: int, cell_height: int):
        '''Draws the cell on the screen at its position'''
        if self.type != 0:
            pygame.draw.rect(screen, self.color, (self.col * cell_width, self.row * cell_height, cell_width, cell_height))