import pygame as pg
import math
pg.init()

W=pg.display.Info().current_w
H=pg.display.Info().current_h

screen = pg.display.set_mode((W, H))

screen.fill("White")
clock = pg.time.Clock()
running = True
per=100

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
    global per
    t=200
    o=75
    pg.draw.rect(screen, "Gold", (t - slider.rect_w / 2-3, o -slider.rect_h/4-3, slider.rect_w+6, slider.rect_h/2+6))
    pg.draw.rect(screen, "Gray", (t - slider.rect_w / 2, o -slider.rect_h/4, slider.rect_w, slider.rect_h/2))
    pg.draw.rect(screen, "Green", (t - slider.rect_w / 2, o -slider.rect_h/4, per/100*slider.rect_w, slider.rect_h/2))
    font1 = pg.font.SysFont('Comic Sans MS', math.floor(slider.rect_h/2), bold=pg.font.Font.bold)
    img1 = font1.render(str(int(per)), True, 'Black')
    screen.blit(img1, (t - slider.rect_w / 2, o-slider.rect_h/2.5))


pg.draw.rect(screen, "Gray", (W / 2 - slider.rect_w / 2, H / 2 + slider.rect_h/2 - slider.rect_h / 2, slider.rect_w, slider.rect_h/2))
pg.draw.rect(screen, "White", (slider.x, slider.y, slider.rect_h, slider.rect_h))
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("White")
    DrawSlider()
    pg.display.update()
    clock.tick(60)

pg.quit()
