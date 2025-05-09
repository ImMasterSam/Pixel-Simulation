import pygame
import math
from Cell import Cell
from Cells.Solid.Moveable.sand import Sand
from Cells.Solid.Immoveable.rock import Rock
from Cells.Liquid.water import Water
from Cells.Liquid.oil import Oil

class Grid:

    Cell_Type = {
        "Empty": 0,
        "Sand": 1,
        "Water": 2,
        "Rock": 3,
        "Oil": 4,
    }
    Cell_Enum = {x : y for y, x in Cell_Type.items()}

    def __init__(self, rows: int, cols: int, width: int, height: int):
        self.rows = rows
        self.cols = cols

        self.width = width
        self.height = height
        self.cell_width = width // cols
        self.cell_height = height // rows

        self.mouse_pressed = False
        self.mouse_erase = False
        self.mouse_grid_pos = (0, 0)
        self.place_cell_type = 1
        self.place_range = 1

        self.iteration = 0
        self.grid = [[Cell(self, r, c) for c in range(cols)] for r in range(rows)]

    # Main functions
    def update(self):
        '''Updates every cells of the grid'''

        mouse_pos = pygame.mouse.get_pos()
        self.mouse_grid_pos = (mouse_pos[0] // self.cell_width, mouse_pos[1] // self.cell_height)

        if self.mouse_pressed:
            sel_range = self.selectRange(self.mouse_grid_pos[1], self.mouse_grid_pos[0])
            self.addCells(sel_range)

        
        for row in range(self.rows-1, -1, -1):
            for col in range(self.cols):
                self.grid[row][col].updated = False

        for row in range(self.rows-1, -1, -1):
            if self.iteration % 2 == 0:
                for col in range(self.cols):
                    if not self.grid[row][col].updated:
                        self.grid[row][col].update()
                        self.grid[row][col].updated = True
            else:
                for col in range(self.cols-1, -1, -1):
                    if not self.grid[row][col].updated:
                        self.grid[row][col].update()

        self.iteration += 1


    def render(self, screen):
        '''Draws every cells of the grid on the screen'''

        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col].render(screen, self.cell_width, self.cell_height)

        # Mouse Range
        grid_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        sel_range = self.selectRange(self.mouse_grid_pos[1], self.mouse_grid_pos[0])
        for row, col in sel_range:
            pygame.draw.rect(grid_surface, (196, 196, 196, 128), (col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height))
        
        screen.blit(grid_surface, (0, 0))


    def handlEvents(self, event: pygame.event.Event):
        '''Handles every events'''
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_pressed = True
            if event.button == 3:
                self.mouse_pressed = True
                self.mouse_erase = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_pressed = False
            if event.button == 3:
                self.mouse_pressed = False
                self.mouse_erase = False
        if event.type == pygame.MOUSEWHEEL:
            self.place_range += event.y
            if self.place_range < 1:
                self.place_range = 1
            if self.place_range > 10:
                self.place_range = 10

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.place_cell_type = 1
            if event.key == pygame.K_2:
                self.place_cell_type = 2
            if event.key == pygame.K_3:
                self.place_cell_type = 3
            if event.key == pygame.K_4:
                self.place_cell_type = 4
            if event.key == pygame.K_r:
                self.grid = [[Cell(self, r, c) for c in range(self.cols)] for r in range(self.rows)]

                
    # Cell functions
    def selectRange(self, row: int, col: int) -> list[tuple[int, int]]:
        '''Returns a list of cells in the range of the given cell'''

        positions = []

        for i in range(-self.place_range + 1, self.place_range):
            for j in range(-self.place_range + 1, self.place_range):

                if math.sqrt(i**2 + j**2) >= self.place_range:
                    continue

                next_row = row + i
                next_col = col + j

                if not ((next_row >= 0 and next_row < self.rows) and (next_col >= 0 and next_col < self.cols)):
                    continue

                positions.append((next_row, next_col))

        return positions

    def addCells(self, pos: list[tuple[int, int]]):
        '''Adds a cell to the grid at the given position'''

        for row, col in pos:

            if self.mouse_erase:
                if self.grid[row][col].type == 0:
                    continue
                self.grid[row][col] = Cell(self, row, col)
            else:         
                if self.grid[row][col].type != 0:
                    continue
                
                match self.place_cell_type:
                    case 1:
                        self.grid[row][col] = Sand(self, row, col)
                    case 2:
                        self.grid[row][col] = Water(self, row, col)
                    case 3:
                        self.grid[row][col] = Rock(self, row, col)
                    case 4:
                        self.grid[row][col] = Oil(self, row, col)

    def getCellType(self, row: int, col: int) -> int:
        '''Returns the type of the cell at the given position'''

        # Check if the row and col are within bounds
        # Return None if out of bounds
        if (row >= 0 and row < self.rows) and (col >= 0 and col < self.cols):
            return self.grid[row][col].type
        else:
            return None
        
    def swapCell(self, row1: int, col1: int, row2: int, col2: int):
        if (row1 >= 0 and row1 < self.rows) and (col1 >= 0 and col1 < self.cols) and (row2 >= 0 and row2 < self.rows) and (col2 >= 0 and col2 < self.cols):
            
            self.grid[row1][col1], self.grid[row2][col2] = self.grid[row2][col2], self.grid[row1][col1]
            # Update positions
            self.grid[row1][col1].row, self.grid[row1][col1].col = row1, col1
            self.grid[row2][col2].row, self.grid[row2][col2].col = row2, col2