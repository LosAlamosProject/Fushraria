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
    def __init__(self, per, rect_w, rect_h, A):
        self.per = per
        self.rect_w = rect_w
        self.rect_h = rect_h
        self.A = A
        self.x = W / 2 - rect_w / 2
        self.y = H / 2 - rect_h / 2

slider = Button(0, 300, 30, False)

def DrawSlider():
    if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[1] >= slider.y - slider.rect_h / 2 and pg.mouse.get_pos()[1] <= slider.y + slider.rect_h / 2 and pg.mouse.get_pos()[0] >= W / 2 - slider.rect_w / 2-slider.rect_h/2 and pg.mouse.get_pos()[0] <= W / 2 + slider.rect_w / 2+slider.rect_h/2 or slider.A):
        slider.x = pg.mouse.get_pos()[0]
        if (pg.mouse.get_pressed()[0] == True):
            slider.A = True
        else:
            slider.A = False
    if (slider.x > W / 2 + slider.rect_w / 2):
        slider.x = W / 2 + slider.rect_w / 2
    if (slider.x < W / 2 - slider.rect_w / 2):
        slider.x = W / 2 - slider.rect_w / 2
    per=(slider.x - W/2 + slider.rect_w / 2) / slider.rect_w*100
    print(per)
    pg.draw.rect(screen, "Gray", (W / 2 - slider.rect_w / 2-slider.rect_h/2, H / 2 -slider.rect_h/4, slider.rect_w+slider.rect_h, slider.rect_h/2))
    pg.draw.rect(screen, "Green", (W / 2 - slider.rect_w / 2-slider.rect_h/2, H / 2 -slider.rect_h/4, slider.rect_w+slider.rect_h - (slider.rect_w + slider.rect_h - (slider.x - (W / 2 - slider.rect_w / 2-slider.rect_h/2))), slider.rect_h/2))
    pg.draw.rect(screen, "White", (slider.x - slider.rect_h / 2, slider.y, slider.rect_h, slider.rect_h))

pg.draw.rect(screen, "Gray", (W / 2 - slider.rect_w / 2, H / 2+slider.rect_h/2 - slider.rect_h / 2, slider.rect_w, slider.rect_h/2))
pg.draw.rect(screen, "White", (slider.x, slider.y, slider.rect_h, slider.rect_h))
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("Black")
    DrawSlider()
    pg.display.update()
    clock.tick(60)

pg.quit()
