from Cell import Cell

class Solid(Cell):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)


class MoveableSolid(Solid):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)

    def update(self):
        '''Moveable solids can move down or sideways'''
        offsets = [0, -1, 1] 

        for offset in offsets:
            next_row = self.row + 1
            next_col = self.col + offset

            next_type = self.grid.getCellType(next_row, next_col)
            if next_type == 0 or next_type == 2: 
                self.grid.swapCell(self.row, self.col, next_row, next_col)
                break 

class UnmoveableSolid(Solid):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)

    def update(self):
        '''Unmoveable solids do not update'''
        pass