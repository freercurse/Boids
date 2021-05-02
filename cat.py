import math
import random
import pygame
from util import catDist


class Cat(pygame.sprite.Sprite):
    def __init__(self, envSize):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create sprite variables and get the rect size
        self.dims = envSize
        self.angle = random.random() * 360
        self.turning = 0
        self.dist = 100
        self.sameDir = 70
        self.toClose = self.dist * 0.4

        self.surf = pygame.Surface((15, 25))
        self.surf.set_colorkey((0, 0, 0))
        self.ogColour = (255,0,0)
        self.surf.fill(self.ogColour)

        self.rect = self.surf.get_rect()
        self.rect.x = envSize['width'] * random.random()
        self.rect.y = envSize['height'] * random.random()

    def update(self, screen, cat,mouse):
        # given the env inputs what does it want to do
        temp, forward, ideal = self.move(cat,mouse, screen)

        self.turning += temp
        self.turning = 0 if abs(self.turning) > 5 else self.turning
        self.angle += self.turning
        self.angle = self.angle % 360

        # turn the agent
        center = self.rect.center
        temp = pygame.transform.rotate(self.surf, self.angle)
        self.rect = temp.get_rect()
        self.rect.center = center

        # movement stuff
        offset = -90
        scalar = 0.01
        self.rect.x += (math.cos(math.radians(self.angle + offset)) + (scalar * ideal[0])/self.dist) * forward
        self.rect.y -= (math.sin(math.radians(self.angle + offset)) + (scalar * ideal[1])/self.dist) * forward

        self.rect.x = self.dims['width'] - self.rect.width if self.rect.x < 15 - self.rect.width else self.rect.x
        self.rect.y = self.dims['height'] - self.rect.height if self.rect.y < 15 - self.rect.height else self.rect.y

        self.rect.x = 0 if self.rect.x >= self.dims['width'] else self.rect.x
        self.rect.y = 0 if self.rect.y >= self.dims['height'] else self.rect.y

        screen.blit(temp, self.rect)

    def move(self, cat,mouse, screen):
        inRange = []
        for cats in cat:
            for mouses in mouse:
                dist = catDist(mouses, cats, self.dims)
                if self.toClose <= dist <= self.dist:
                    inRange.append(mouses)
                    pygame.draw.line(screen, (50, 50, 50),
                                     (cats.rect.x + cats.rect.width/2, cats.rect.y + cats.rect.height/2),
                                     (mouses.rect.x + mouses.rect.width/2, mouses.rect.y + mouses.rect.height/2), 2)

        avDir = 0
        close = []
        for x in inRange:
            avDir += (x.angle / len(inRange))
            if (x.angle > 360 - self.sameDir/2 < self.angle or x.angle < self.sameDir/2 > self.angle) or (abs(x.angle - self.angle) < self.sameDir):
                close.append(x)
            else:
                x.surf.fill(x.ogColour)

        diff = avDir - self.angle
        avxy = []
        if len(close) == 0:
            self.surf.fill(self.ogColour)

        avColour = [0, 0, 0]
        scalar = 0.75
        for cats in close:
            avColour = [x + y for x, y in zip(cats.ogColour, avColour)]
            avxy.append([cats.rect.x / (scalar * len(close)), cats.rect.y / (scalar * len(close))])

        if len(close) > 0:
            self.surf.fill([(x/len(close)) for x in avColour])

        if avxy != []:
            temp = [0,0]
            for x in avxy:
                temp[0] += x[0]
                temp[1] += x[1]
            avxy = [self.rect.x - temp[0], self.rect.y - temp[1]]
        else:
            avxy = [0, 0]
        if 0 < abs(diff) < 1:
            diff = 1 * (diff/diff)

        if len(close) == 0:
            diff = random.random() * 2
        return diff / 10, 5, avxy
