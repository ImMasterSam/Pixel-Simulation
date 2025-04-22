import pygame
from player import player
from Grid import Grid
import asyncio

Screen_width = 600
Screen_height = 400

pygame.init()

screen = pygame.display.set_mode((600, 400))
bg = pygame.Surface(screen.get_size())
bg.fill((0, 0, 0))

# play = player(50, 50, 50)
# sg = pygame.sprite.Group()
# sg.add(play)

main_grid = Grid(80, 120, 600, 400)

async def main():

    clock = pygame.time.Clock()
    Running = True

    while Running:

        clock.tick(60)

        for event in pygame.event.get():
            main_grid.handlEvents(event)
            if event.type == pygame.QUIT:
                Running = False

        main_grid.update()

        screen.blit(bg, (0, 0))
        main_grid.render(screen)
        pygame.display.update()

        await asyncio.sleep(0)

    

asyncio.run(main())
pygame.quit()