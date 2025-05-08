import pygame
from random import choice
from Cell import Cell

class Water(Cell):

    color_list = [(0, 0, 255), (30, 30, 255), (50, 50, 255)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 2)  # 2 for water type
        self.color = choice(self.color_list)

    def update(self):

        # Falling down
        offsets = [0, -1, 1] 

        for offset in offsets:
            next_row = self.row + 1
            next_col = self.col + offset

            next_type = self.grid.getCellType(next_row, next_col)
            if next_type == 0: 
                self.grid.swapCell(self.row, self.col, next_row, next_col)
                return
            
        # Horizontal movement
        # Check left cells
        offset = 1
        left = None

        while True:

            right_type = self.grid.getCellType(self.row, self.col - offset)
            under_type = self.grid.getCellType(self.row + 1, self.col - offset)

            if right_type != 0:
                break

            if under_type == 0:
                left = -offset
                break

            offset += 1

        # Check right cells
        offset = 1
        right = None

        while True:

            right_type = self.grid.getCellType(self.row, self.col + offset)
            under_type = self.grid.getCellType(self.row + 1, self.col + offset)

            if right_type != 0:
                break

            if under_type == 0:
                right = offset
                break

            offset += 1

        # Check if the water can move left or right
        if left is not None and right is not None:
            if abs(left) < abs(right):
                self.grid.swapCell(self.row, self.col, self.row, self.col + left)
            else:
                self.grid.swapCell(self.row, self.col, self.row, self.col + right)
        elif left is not None:
            self.grid.swapCell(self.row, self.col, self.row, self.col + left)
        elif right is not None:
            self.grid.swapCell(self.row, self.col, self.row, self.col + right)


    def render(self, screen, cell_width: int, cell_height: int):
        pygame.draw.rect(screen, self.color, (self.col * cell_width, self.row * cell_height, cell_width, cell_height))