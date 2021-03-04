# https://github.com/futurelucas4502

import pygame
from fish import Fish
from util import excluded

# Initialise
dims = {'width': 1000, 'height': 900}
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((dims['width'], dims['height']))
running = True

# Instantiate player.
fish = [Fish(dims) for x in range(100)]


while running:
    # Set FPS
    clock.tick(10)

    # Main game
    screen.fill((0, 0, 0))
    [fishy.update(screen, others) for fishy, others in zip(fish, excluded(fish))]


    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()