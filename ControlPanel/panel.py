import pygame
from ControlPanel.button import Button

class Panel:

    bg_color = (150, 150, 150, 70)

    cell_type = {
        "Sand": 1,
        "Water": 2,
        "Rock": 3,
        "Oil": 4,
    }
    cell_enum = {x : y for y, x in cell_type.items()}
    cell_color = [(0, 0, 0), (255, 255, 0), (0, 0, 255), (128, 128, 128), (50, 0, 0)]

    def __init__(self, x: int, y: int, scale: int = 25, margin: int = 10):

        self.x = x
        self.y = y
        self.width = scale * len(self.cell_type) + margin * (len(self.cell_type) + 1)
        self.height = scale + margin * 2

        self.scale = scale
        self.margin = margin

        self.bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.bg.fill(self.bg_color)

        self.buttons: list[Button] = []

        for i in range(1, len(self.cell_color)):
            self.buttons.append(Button(self.getResolutePos(i - 1), scale, margin, self.cell_color[i]))

        self.open = False
        self.place_cell_type = 1

    def render(self, screen: pygame.Surface):
        '''Draws the panel on the screen'''
        if not self.open:
            return
        
        self.bg.fill(self.bg_color)
        screen.blit(self.bg, (self.x, self.y))

        for button in self.buttons:
            button.render(screen)

    def update(self, mouse_pos: tuple[int, int]):
        '''Updates the panel'''
        for button in self.buttons:
            button.update(mouse_pos, self.open)
        
        self.buttons[self.place_cell_type - 1].selected = True

    def handleEvents(self, event: pygame.event.Event):
        '''Handles events for the panel'''
        for i, button in enumerate(self.buttons):
            if button.handleEvents(event):
                self.place_cell_type = i + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.open = not self.open

    def ishover(self, mouse_pos: tuple[int, int]) -> bool:
        '''Checks if the mouse is hovering over the panel'''
        if self.open:
            return self.x < mouse_pos[0] < self.width + self.x and self.y < mouse_pos[1] < self.height + self.y
        return False

    # Calculate Function
    def getResolutePos(self, idx: int) -> tuple[int, int]:
        '''Get the relative position of the mouse on the panel'''
        x = self.x + (idx % len(self.cell_color)) * self.scale + (idx % len(self.cell_color) + 1) * self.margin
        y = self.y + (idx // len(self.cell_color)) * self.scale + (idx // len(self.cell_color) + 1) * self.margin
        return x, y
