import pygame
from helper import *
import intro
import level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
b = pygame.image.load("assets/ui/background.jpg")

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    if intro.inIntro:
        intro.showIntro(screen, WIDTH, HEIGHT)
    else:
        level.showLevel(screen)
    pygame.display.update()
pygame.quit()
