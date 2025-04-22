import pygame
from Cell import Cell

class Grid:

    Cell_Type = {
        "Empty": 0,
        "Sand": 1,
        "Water": 2,
        "Rock": 3,
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

        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_col = mouse_pos[0] // self.cell_width
        mouse_row = mouse_pos[1] // self.cell_height

        if self.mouse_pressed:
            self.addCell(mouse_row, mouse_col, 1)

        for row in range(self.rows-1, -1, -1):
            for col in range(self.cols-1, -1, -1):
                self.grid[row][col].update()

    def render(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell: Cell = self.grid[row][col]
                cell.render(screen, self.cell_width, self.cell_height)

    def handlEvents(self, event: pygame.event.Event):
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_pressed = False

    def addCell(self, row: int, col: int, type: int):
        if row < self.rows and col < self.cols:
            self.grid[row][col] = Cell(row, col, type)