import pygame
from Grid import Grid
from Text.FPS import FPS
import asyncio

Rows = 100
Cols = 100
Screen_width = 500
Screen_height = 500
TargetFPS = 60

pygame.init()

pygame.display.set_caption("Pixel Simulation")
screen = pygame.display.set_mode((Screen_width, Screen_height))
bg = pygame.Surface(screen.get_size())
bg.fill((0, 0, 0))

main_grid = Grid(Rows, Cols, Screen_width, Screen_height)
fps = FPS(TargetFPS)

async def main():

    clock = pygame.time.Clock()
    Running = True

    while Running:

        clock.tick(TargetFPS)

        for event in pygame.event.get():
            main_grid.handlEvents(event)
            if event.type == pygame.QUIT:
                Running = False

        main_grid.update()
        fps.update()

        screen.blit(bg, (0, 0))
        main_grid.render(screen)
        fps.render(screen)
        pygame.display.update()

        await asyncio.sleep(0)

    

asyncio.run(main())
pygame.quit()