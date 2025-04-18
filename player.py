import pygame

class player(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos, size):

        super().__init__()
        self.size = size
        self.movement = [0, 0]
        self.pos = (xpos, ypos)

        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.pos = (self.pos[0] + self.movement[0]*2, self.pos[1] + self.movement[1]*2)
        self.rect.topleft = self.pos
        pass

    def handlEvents(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.movement[1] -= 1
            if event.key == pygame.K_a:
                self.movement[0] -= 1
            if event.key == pygame.K_s:
                self.movement[1] += 1
            if event.key == pygame.K_d:
                self.movement[0] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.movement[1] += 1
            if event.key == pygame.K_a:
                self.movement[0] += 1
            if event.key == pygame.K_s:
                self.movement[1] -= 1
            if event.key == pygame.K_d:
                self.movement[0] -= 1
        pass