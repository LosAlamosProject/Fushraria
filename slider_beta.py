import pygame as pg
import math
pg.init()

W = 500
H = 420
screen = pg.display.set_mode((W, H))
screen.fill("Black")
clock = pg.time.Clock()
running = True

rect_w = 300
rect_h = 30
x = W / 2 - rect_w / 2
y = H / 2 - rect_h / 2
pg.draw.rect(screen, "Gray", (W / 2 - rect_w / 2, H / 2 - rect_h / 2, rect_w, rect_h))
pg.draw.rect(screen, "White", (x, y, rect_h, rect_h))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #screen.fill("Black")
    if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[1] >= y - rect_h / 2 and pg.mouse.get_pos()[1] <= y + rect_h / 2 and pg.mouse.get_pos()[0] >= x - rect_h / 2 and pg.mouse.get_pos()[0] <= x + rect_h / 2):
        x = pg.mouse.get_pos()[0]
    screen.fill("Black")
    pg.draw.rect(screen, "Gray", (W / 2 - rect_w / 2, H / 2 - rect_h / 2, rect_w, rect_h))
    pg.draw.rect(screen, "White", (x, y, rect_h, rect_h))
    pg.display.update()
    clock.tick(60)

pg.quit()