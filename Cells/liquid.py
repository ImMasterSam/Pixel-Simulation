from random import choice
from Cell import Cell


class Liquid(Cell):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)
        self.dispersionRate = 0
        
        self.velocity = 1
        self.isFreeFalling = True

    def update(self):

        # Falling down
        if self.isFreeFalling:
            self.velocity += self.gravity
            step = int(self.velocity)

            fall_dis = 0

            for i in range(1, step + 1):
                if self.grid.getCellInfo(self.row + i, self.col)['type'] != 0:
                    break
                else:
                    fall_dis = i

            if fall_dis != step:
                self.isFreeFalling = False
                self.velocity = 1

            self.grid.swapCell(self.row, self.col, self.row + fall_dis, self.col)
            
        else:

            # Sinking
            next_cell = self.grid.getCellInfo(self.row + 1, self.col)
            if next_cell['type'] != 0 and next_cell['density'] < self.density: 
                self.grid.swapCell(self.row, self.col, self.row + 1, self.col)
                self.updated = True
                return

            # Horizontal dispersion
            left, right = 0, 0

            # Check left cells
            for i in range(1, self.dispersionRate + 1):
                if self.grid.getCellInfo(self.row, self.col - i)['density'] >= self.density:
                    break
                else:
                    left = -i
                    

            # Check right cells
            for i in range(1, self.dispersionRate + 1):
                if self.grid.getCellInfo(self.row, self.col + i)['density'] >= self.density:
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

            # Check bottom, if empty then free fall
            offsets = [0, -1, 1] 

            for offset in offsets:
                next_row = self.row + 1
                next_col = self.col + offset

                next_type = self.grid.getCellInfo(next_row, next_col)['type']
                if next_type == 0: 
                    self.grid.swapCell(self.row, self.col, next_row, next_col)
                    self.isFreeFalling = True

        self.updated = True

