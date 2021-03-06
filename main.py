# https://github.com/futurelucas4502

import pygame
from fish import Fish
from util import excluded

# Initialise
# dims = {'width': 500, 'height': 500}
dims = {'width': 1920, 'height': 1080}
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((dims['width'], dims['height']))
running = True

# Instantiate player.
fish = [Fish(dims) for x in range(100)]

while running:
    # Set FPS
    clock.tick(20)

    # Main game
    screen.fill((0, 0, 0))
    rng = fish[0].dist
    pygame.draw.line(screen, (255, 0, 0), (rng/2, rng/2), (rng/2, dims['height'] - rng/2))
    pygame.draw.line(screen, (255, 0, 0), (rng/2, dims['height'] - rng/2), (dims['width'] - rng/2, dims['height'] - rng/2))
    pygame.draw.line(screen, (255, 0, 0), (dims['width'] - rng/2, dims['height'] - rng/2), (dims['width'] - rng/2, rng/2))
    pygame.draw.line(screen, (255, 0, 0), (dims['width'] - rng/2, rng/2), (rng/2, rng/2))

    [fishy.update(screen, others) for fishy, others in zip(fish, excluded(fish))]

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()
