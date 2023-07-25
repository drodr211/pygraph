import pygame
from array import *
import time

pygame.init()

screenSize = 500
window = pygame.display.set_mode((screenSize, screenSize))
FONT = pygame.font.Font(pygame.font.get_default_font(), 36)
black = (0,0,0)

xymax = 10
scale = screenSize/xymax

run = True
while run:
    window.fill((204, 204, 204))

    ytext = FONT.render("- " + str(xymax), True, (0, 0, 0))
    xtext = FONT.render( str(xymax), True, (0, 0, 0))

    for x in range(0,screenSize):
        xf = x*scale
        y = xf
        pygame.draw.circle(window, black, (x*scale,(screenSize-y)), 1)

    #pygame.draw.rect(window, black, graphBox, 1)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(ytext, dest=(0,0))
    window.blit(xtext, dest=(screenSize-70,screenSize-40))
    pygame.display.flip()
pygame.quit()

