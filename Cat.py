import pygame as pg
from random import randint, uniform
vec = pg.math.Vector2

WIDTH = 1024
HEIGHT = 768
RED = (255, 0, 0)

# Mob properties
CAT_SIZE = 18
MAX_SPEED = 2.5
MAX_FORCE = 0.5


class Cat(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((CAT_SIZE, CAT_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0, WIDTH), randint(0, HEIGHT))
        self.vel = vec(MAX_SPEED, 0).rotate(uniform(0, 360))
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.randcords = [randint(0, WIDTH), randint(0, HEIGHT)]
        self.State = 1  # 1 = wander 2 = Seek/Evade

    def StateChange(self):
        if self.State == 1:
            self.State += 1
        else:
            self.State -=1


    def calcCoords(self):

        self.randcords = [randint(0, WIDTH), randint(0, HEIGHT)]

    def wander(self):

        self.desired = (self.randcords - self.pos) * MAX_SPEED

        steer = (self.desired - self.vel)
        if steer.length() > MAX_FORCE:
            steer.scale_to_length(MAX_FORCE)
        return steer


    def seek(self, target):
        self.desired = (target - self.pos) * MAX_SPEED
        steer = (self.desired - self.vel)
        if steer.length() > MAX_FORCE:
            steer.scale_to_length(MAX_FORCE)
        return steer

    def update(self, positions):
        # self.follow_mouse()
        if self.State == 1:
            self.acc = self.wander()
        else:
            self.acc = self.seek(positions[1])

        # equations of motion
        self.vel += self.acc
        if self.vel.length() > MAX_SPEED:
            self.vel.scale_to_length(MAX_SPEED)
        self.pos += self.vel
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.center = self.pos

