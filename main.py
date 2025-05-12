import asyncio
import pygame
from Grid import Grid
from Text.FPS import FPS
from Text.TypeText import TypeText
from ControlPanel.Panel import Panel


Rows = 200
Cols = 200
Screen_width = 800
Screen_height = 800
TargetFPS = 60

pygame.init()

pygame.display.set_caption("Pixel Simulation")
screen = pygame.display.set_mode((Screen_width, Screen_height))
bg = pygame.Surface(screen.get_size())
bg.fill((0, 0, 0))

main_grid = Grid(Rows, Cols, Screen_width, Screen_height)
panel = Panel()
fps = FPS(TargetFPS, Screen_width - 60)
typeText = TypeText()

async def main():

    clock = pygame.time.Clock()
    Running = True

    while Running:

        clock.tick(TargetFPS)

        for event in pygame.event.get():
            main_grid.handlEvents(event)
            panel.handleEvents(event)
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Running = False

        mouse_pos = pygame.mouse.get_pos()
        main_grid.update(mouse_pos, panel)
        panel.update(mouse_pos)
        typeText.update(panel)
        fps.update()

        screen.blit(bg, (0, 0))
        main_grid.render(screen)
        panel.render(screen)
        typeText.render(screen)
        fps.render(screen)
        pygame.display.update()

        await asyncio.sleep(0) 

asyncio.run(main())