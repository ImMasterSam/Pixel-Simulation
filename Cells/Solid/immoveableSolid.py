from Cells.solid import Solid

class ImmoveableSolid(Solid):

    def __init__(self, grid, row: int, col: int, type: int = 0):
        super().__init__(grid, row, col, type)

    def update(self):
        '''Unmoveable solids do not update'''
        self.updated = True