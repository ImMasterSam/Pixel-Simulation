from random import choice
from Cell import Cell

class Liquid(Cell):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)
        self.dispersionRate = 0

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
        left, right = 0, 0

        # Check left cells
        for i in range(1, self.dispersionRate + 1):
            if self.grid.getCellType(self.row, self.col - i) != 0:
                break
            else:
                left = -i
                

        # Check right cells
        for i in range(1, self.dispersionRate + 1):
            if self.grid.getCellType(self.row, self.col + i) != 0:
                break
            else:
                right = i

        if abs(left) > 0 and abs(right) > 0:
            if abs(left) < abs(right):
                self.grid.swapCell(self.row, self.col, self.row, self.col + right)
            elif abs(left) > abs(right):
                self.grid.swapCell(self.row, self.col, self.row, self.col + left)
            else:
                step = choice([-1, 1])
                self.grid.swapCell(self.row, self.col, self.row, self.col + right * step)
        elif abs(left) > 0:
            self.grid.swapCell(self.row, self.col, self.row, self.col + left)
        elif abs(right) > 0:
            self.grid.swapCell(self.row, self.col, self.row, self.col + right)

