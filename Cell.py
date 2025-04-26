import pygame

class Cell:

    def __init__(self, grid, row: int, col: int, type: int = 0):
        self.grid = grid
        self.row = row
        self.col = col
        self.type = type

    def update(self):
        '''Override this method in subclasses to define the behavior of the cell'''
        pass
    
    def render(self):
        '''Override this method in subclasses to define how the cell is drawn'''
        pass