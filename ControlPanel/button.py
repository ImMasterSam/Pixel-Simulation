import pygame

class Button:

    def __init__(self, pos: tuple[int, int], scale: int, border: int, color: tuple[int, int, int]):
        self.pos = pos
        self.scale = scale
        self.border = border
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], scale, scale)
        self.hover = False
        self.active = False
        self.selected = False

    def update(self, mouse_pos: tuple[int, int], active: bool):
        '''Updates the button state based on mouse position'''
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False

        self.active = active
        self.selected = False

    def render(self, surface: pygame.Surface):
        '''Draws the button on the surface'''
        pygame.draw.rect(surface, self.color, self.rect)

        if self.hover:
            pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)

        if self.selected:
            pygame.draw.rect(surface, (0, 255, 0), self.rect, 1)

    def handleEvents(self, event: pygame.event.Event) -> bool:
        '''Handles events for the button'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hover and self.active:
            return True
        else:
            return False