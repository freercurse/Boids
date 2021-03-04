import pygame
import math
from pygame.locals import *
import random


class Fish(pygame.sprite.Sprite):
    def __init__(self, envSize):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create sprite variables and get the rect size
        self.dims = envSize
        self.angle = random.random() * 360
        self.turning = 0

        self.surf = pygame.Surface((10, 20))
        self.surf.set_colorkey((0, 0, 0))
        self.surf.fill((random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)))

        self.rect = self.surf.get_rect()
        self.rect.x = envSize['width'] * random.random()
        self.rect.y = envSize['height'] * random.random()

    def update(self, screen, fish):
        # given the env inputs what does it want to do
        temp, forward = self.move(fish)

        self.turning += temp
        self.turning = 0 if abs(self.turning) > 20 else self.turning
        self.angle += self.turning

        # turn the agent
        center = self.rect.center
        temp = pygame.transform.rotate(self.surf, self.angle)
        self.rect = temp.get_rect()
        self.rect.center = center

        # movement stuff
        offset = -90
        self.rect.x += math.cos(math.radians(self.angle + offset)) * forward
        self.rect.y -= math.sin(math.radians(self.angle + offset)) * forward

        self.rect.x = self.dims['width'] - self.rect.width if self.rect.x < 0 - self.rect.width else self.rect.x
        self.rect.y = self.dims['height'] - self.rect.height if self.rect.y < 0 - self.rect.height else self.rect.y

        self.rect.x = 0 if self.rect.x > self.dims['width'] else self.rect.x
        self.rect.y = 0 if self.rect.y > self.dims['height'] else self.rect.y


        screen.blit(temp, self.rect)

    def move(self, fish):
        return (random.random()-0.5) * 2, 5
