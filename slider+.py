import pygame as pg
import math
pg.init()

W = 500
H = 420
screen = pg.display.set_mode((W, H))
screen.fill("Black")
clock = pg.time.Clock()
running = True

class Button:
    def __init__(self, rect_w, rect_h, A):
        self.rect_w = rect_w
        self.rect_h = rect_h
        self.A = A
        self.x = W / 2 - rect_w / 2
        self.y = H / 2 - rect_h / 2
    def DrawSlider(self):
        global W, H
        if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[1] >= self.y - self.rect_h / 2 and pg.mouse.get_pos()[1] <= self.y + self.rect_h / 2 and pg.mouse.get_pos()[0] >= W / 2 - self.rect_w / 2-self.rect_h/2 and pg.mouse.get_pos()[0] <= W / 2 + self.rect_w / 2+self.rect_h/2 or self.A):
            self.x = pg.mouse.get_pos()[0]
            if (pg.mouse.get_pressed()[0] == True):
                self.A = True
            else:
                self.A = False
        if (self.x > W / 2 + self.rect_w / 2):
            self.x = W / 2 + self.rect_w / 2
        if (self.x < W / 2 - self.rect_w / 2):
            self.x = W / 2 - self.rect_w / 2
        per=(self.x - W/2 + self.rect_w / 2) / self.rect_w*100
        print(per)
        pg.draw.rect(screen, "Gray", (W / 2 - self.rect_w / 2-self.rect_h/2, H / 2 -self.rect_h/4, self.rect_w+self.rect_h, self.rect_h/2))
        pg.draw.rect(screen, "Green", (W / 2 - self.rect_w / 2-self.rect_h/2, H / 2 -self.rect_h/4, self.rect_w+self.rect_h - (self.rect_w + self.rect_h - (self.x - (W / 2 - self.rect_w / 2-self.rect_h/2))), self.rect_h/2))
        pg.draw.rect(screen, "White", (self.x - self.rect_h / 2, self.y, self.rect_h, self.rect_h))

slider = Button(300, 30, False)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("Black")
    slider.DrawSlider()
    pg.display.update()
    clock.tick(60)

pg.quit()
