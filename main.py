import pygame
from player import player
import asyncio

pygame.init()

screen = pygame.display.set_mode((600, 400))
bg = pygame.Surface(screen.get_size())
bg.fill((0, 0, 255))

play = player(50, 50, 50)
sg = pygame.sprite.Group()
sg.add(play)

async def main():

    clock = pygame.time.Clock()
    Running = True

    while Running:

        clock.tick(60)

        for event in pygame.event.get():
            play.handlEvents(event)
            if event.type == pygame.QUIT:
                Running = False

        play.update()

        screen.blit(bg, (0, 0))
        sg.draw(screen)
        pygame.display.update()

        await asyncio.sleep(0)

    

asyncio.run(main())
pygame.quit()