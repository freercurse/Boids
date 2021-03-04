# https://github.com/futurelucas4502

import pygame
from fish import Fish

# Initialise
dims = {'width': 1800,
        'height': 900}
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((dims['width'], dims['height']))
running = True

# Instantiate player.
fish = [Fish(dims) for x in range(10)]


while running:
    # Set FPS
    clock.tick(1)

    # Main game
    screen.fill((0, 0, 0))
    [x.update(screen) for x in fish]


    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()