import random
import sys
import pygame
pygame.init()
#Global variables for the game

SCREEN_WIDTH = 1920/2
SCREEN_HEIGHT = 1080/2
CENTER = pygame.math.Vector2(450,250)
RADIUS = 200
COLORS = pygame.colordict.THECOLORS


R_vec = pygame.math.Vector2(0,RADIUS)
CIRCLES = [(pygame.math.Vector2(0,x*RADIUS*0.1), 11-x) for x in range(1,11)]

print(CIRCLES)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    clock.tick(30)
    screen.fill(COLORS['black'])
    pygame.draw.circle(screen, COLORS['white'], CENTER, RADIUS, 1)
    # pygame.draw.line(screen, COLORS['white'],CENTER,CENTER + R_vec)

    for c, speed in CIRCLES:
        pygame.draw.circle(screen, COLORS['red'], CENTER + c, 10)
        c.rotate_ip(speed)

    pygame.display.flip()