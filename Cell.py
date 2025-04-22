import pygame

class Cell:

    def __init__(self, row: int, col: int, type: int = 0):
        self.row = row
        self.col = col
        self.type = type

    def update(self):
        pass
    
    def render(self, screen, cell_width: int, cell_height: int):
        if self.type != 0:
            pygame.draw.rect(screen, (255, 255, 0), (self.col * cell_width, self.row * cell_height, cell_width, cell_height))