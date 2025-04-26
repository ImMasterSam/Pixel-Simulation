import pygame

class FPS:

    def __init__(self, fps: int = 60, x: int = 5, y: int = 5, font_size: int = 20, font_color: tuple = (255, 255, 255)):

        self.TargetFPS = fps
        self.fps = 0
        self.x = x
        self.y = y

        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(f"FPS: {self.fps}", True, self.font_color)
        
        self.clock = pygame.time.Clock()
        self.last_time = pygame.time.get_ticks()

    def update(self):
        '''Update the FPS clock'''
        self.current_time = pygame.time.get_ticks()
        self.fps = 1000 / (self.current_time - self.last_time)
        self.last_time = self.current_time
        self.text_surface = self.font.render(f"FPS: {int(self.fps)}", True, self.font_color)

    def render(self, screen: pygame.Surface):
        '''Render the FPS on the screen'''
        screen.blit(self.text_surface, (self.x, self.y))

