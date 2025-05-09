from random import choice
from Cells.Liquid import Liquid

class Water(Liquid):
    '''
    # Water Cell
    - liquid type
    - color: blue shades
    - dispersion rate: 1 (default)
    '''

    color_list = [(0, 0, 255), (30, 30, 255), (50, 50, 255)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 2)  # 2 for water type
        self.color = choice(self.color_list)
        self.dispersionRate = 3

class Oil(Liquid):
    '''
    # Oil Cell
    - liquid type
    - color: Dark Reds shades
    - dispersion rate: 2 (default)
    '''

    color_list = [(50, 20, 0), (70, 20, 0), (100, 20, 0)]

    def __init__(self, grid, row: int, col: int):
        super().__init__(grid, row, col, 4)  # 4 for oil type
        self.color = choice(self.color_list)
        self.dispersionRate = 2

