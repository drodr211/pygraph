import pygame
from array import *
import time

pygame.init()

window = pygame.display.set_mode((700, 500))
graphBox = pygame.Rect(100, 100, 500, 300)
black = (0,0,0)

run = True
while run:
    window.fill((204, 204, 204))

    pygame.draw.rect(window, black, graphBox, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()
pygame.quit()

