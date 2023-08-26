import pygame as pg
import math
pg.init()

W = 700
H = 500
screen = pg.display.set_mode((W, H))
screen.fill("Black")
clock = pg.time.Clock()
running = True

class Button:
    #per je za koliko procenata ce imati healthbar na pocetku
    #rect_w je za sirinu healthbar
    #rect_h je za visinu healthbar
    #X i Y su za poziciju healthbar
    def __init__(self, per, rect_w, rect_h, X, Y):
        self.per = per
        self.rect_w = rect_w
        self.rect_h = rect_h
        self.X = X
        self.Y = Y
        self.x = self.X + self.rect_w * per / 100
        self.y = self.Y
    def DrawSlider(self):
        global W, H
        self.x = self.X + self.rect_w * self.per / 100
        pg.draw.rect(screen, "Gray", (self.X-self.rect_h/2, self.Y, self.rect_w, self.rect_h/2))
        pg.draw.rect(screen, "Green", (self.X-self.rect_h/2, self.Y, self.rect_w+self.rect_h - (self.rect_w + self.rect_h - (self.x - (self.X))), self.rect_h/2))

slider = Button(50, 300, 30, 200, 250)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("Black")
    slider.DrawSlider()
    pg.display.update()
    clock.tick(60)

pg.quit()
