import pygame as pg
from pygame import USEREVENT

from Cat import Cat
from Mouse import Mouse

class main():
    def __init__(self):
        super(self)
        screen = pg.display.get_surface()
        self.width = 800
        self.height = 600
        self.fps = 60
        self.counter = 0


    def start(self):
        pg.init()
        cat = Cat()
        mouse = Mouse()
        screen = pg.display.set_mode((1024, 768))
        clock = pg.time.Clock()
        running = True
        sprite = pg.sprite.Group()
        sprite.add(cat)
        sprite.add(mouse)
        calcCoords = USEREVENT + 1

        pg.time.set_timer(calcCoords, 50)


        while running:

            if pg.event.get(calcCoords):
                mouse.calcCoords()
                cat.calcCoords()

            sprite.update([cat.pos,mouse.pos])
            self.AuraDetection([cat.pos, mouse.pos], cat, mouse)
            clock.tick(60)
            pg.display.set_caption("{:.2f}".format(clock.get_fps()))
            screen.fill((250, 250, 250))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False


            sprite.draw(screen)
            pg.display.flip()

    def AuraDetection(self, animals, cat, mouse):
        if abs(animals[0][0] - animals[1][0]) <= 150 and abs(animals[0][1] - animals[1][1]) <= 150 and self.counter == 0:
            cat.StateChange()
            self.counter = 1






if __name__ == '__main__':
    main.start(main)



