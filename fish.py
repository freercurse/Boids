import pygame
from pygame.locals import *
import random


class Fish(pygame.sprite.Sprite):
    def __init__(self, envSize):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create sprite variables and get the rect size
        self.surf = pygame.Surface((10, 20))
        self.surf.set_colorkey((0, 0, 0))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.envSize = envSize
        self.rect.x = envSize['width'] * random.random()
        self.rect.y = envSize['height'] * random.random()

    def update(self, screen):
        center = self.rect.center
        self.temp = pygame.transform.rotate(self.surf, random.random()*359)
        self.rect = self.temp.get_rect()
        self.rect.center = center

        screen.blit(self.temp, self.rect)
