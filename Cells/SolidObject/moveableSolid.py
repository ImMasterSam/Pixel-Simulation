from random import choice
from Cells.solid import Solid

class MoveableSolid(Solid):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)
        
        # Solid movement variables
        self.velocity: list[float] = [0, 1]
        self.friction = 0
        self.isFreeFalling = True

    def update(self):
        '''Moveable solids can fall down or go sideways'''

        if self.isFreeFalling:
            self.velocity[1] += self.gravity
            step = int(self.velocity[1])

            fall_dis = 0

            for i in range(1, step + 1):
                if self.row + i >= self.grid.rows:
                    break
                if self.grid.gridArray[self.row + i][self.col].type != 0:
                    break
                else:
                    fall_dis = i

            if fall_dis != step:
                self.isFreeFalling = False
                direction = choice([-1, 1])
                self.velocity = [self.velocity[0] + self.velocity[1] * direction, 0]

            self.grid.swapCell(self.row, self.col, self.row + fall_dis, self.col)
            
        else:

            # Check bottom, if empty then free fall of Sink
            offsets = [0, -1, 1] 

            for offset in offsets:
                next_row = self.row + 1
                next_col = self.col + offset

                if next_row >= self.grid.rows or next_col >= self.grid.cols or next_col < 0:
                    continue

                next_cell = self.grid.gridArray[next_row][next_col]
                if next_cell.type == 0: 
                    self.grid.swapCell(self.row, self.col, next_row, next_col)
                    self.isFreeFalling = True
                    self.velocity[1] = 1
                    self.updated = True
                    return
                if next_cell.density < self.density: 
                    self.grid.swapCell(self.row, self.col, next_row, next_col)
                    self.updated = True
                    return
            
            # Horizontal movement
            direction = 1 if self.velocity[0] > 0 else -1
            step = abs(int(self.velocity[0]))
            move = 0

            for i in range(1, step + 1):
                if self.col + i * direction >= self.grid.cols or self.col + i * direction < 0:
                    break
                if self.grid.gridArray[self.row][self.col + i * direction].type != 0:
                    break
                else:
                    move = i
            
            self.velocity[0] *= (1 - self.friction)
            self.grid.swapCell(self.row, self.col, self.row, self.col + move * direction)

        self.updated = True