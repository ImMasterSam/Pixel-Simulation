import pygame
from ControlPanel.Panel import Panel

class TypeText:

    def __init__(self, x: int = 5, y: int = 5, font_size: int = 30, font_color: tuple = (255, 255, 255)):

        self.x = x
        self.y = y

        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(f"None", True, self.font_color)

    def update(self, panel: Panel):
        '''Update The text surface'''
        self.text_surface = self.font.render(f"{panel.cell_enum[panel.place_cell_type]}", True, panel.cell_color[panel.place_cell_type])

    def render(self, screen: pygame.Surface):
        '''Render the FPS on the screen'''
        screen.blit(self.text_surface, (self.x, self.y))

