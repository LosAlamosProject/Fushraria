import pygame as pg
import math
pg.init()

W = 500
H = 420
screen = pg.display.set_mode((W, H))
screen.fill("Black")
clock = pg.time.Clock()
running = True

per=0

rect_w = 300
rect_h = 30
x = W / 2 - rect_w / 2
y = H / 2 - rect_h / 2
pg.draw.rect(screen, "Gray", (W / 2 - rect_w / 2, H / 2+rect_h/2 - rect_h / 2, rect_w, rect_h/2))
pg.draw.rect(screen, "White", (x, y, rect_h, rect_h))
A = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #screen.fill("Black")
    if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[1] >= y - rect_h / 2 and pg.mouse.get_pos()[1] <= y + rect_h / 2 and pg.mouse.get_pos()[0] >= W / 2 - rect_w / 2-rect_h/2 and pg.mouse.get_pos()[0] <= W / 2 + rect_w / 2+rect_h/2 or A):
        x = pg.mouse.get_pos()[0]
        if (pg.mouse.get_pressed()[0] == True):
            A = True
        else:
            A = False
        if (x > W / 2 + rect_w / 2):
            x = W / 2 + rect_w / 2
        if (x < W / 2 - rect_w / 2):
            x = W / 2 - rect_w / 2
    per=(x-W/2+rect_w/2)/rect_w*100
    print(per)
    screen.fill("Black")
    pg.draw.rect(screen, "Gray", (W / 2 - rect_w / 2-rect_h/2, H / 2 -rect_h/4, rect_w+rect_h, rect_h/2))
    pg.draw.rect(screen, "Green", (W / 2 - rect_w / 2-rect_h/2, H / 2 -rect_h/4, rect_w+rect_h - (rect_w + rect_h - (x - (W / 2 - rect_w / 2-rect_h/2))), rect_h/2))
    pg.draw.rect(screen, "White", (x - rect_h / 2, y, rect_h, rect_h))
    pg.display.update()
    clock.tick(60)

pg.quit()
