import pygame as pg
import math
pg.init()

W = 775
H = 500
screen = pg.display.set_mode((W, H))
screen.fill("Black")
clock = pg.time.Clock()
running = True

image = pg.image.load("C:\\Users\\korisnik\\Downloads\\BlueCube.png").convert()
L = [image, 0, 0, 0]

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("Black")
    pg.draw.rect(screen, "Gray", (75, 350, 100, 100))
    pg.draw.rect(screen, "Gray", (250, 350, 100, 100))
    pg.draw.rect(screen, "Gray", (425, 350, 100, 100))
    pg.draw.rect(screen, "Gray", (600, 350, 100, 100))
    screen.blit(L[0], (100, 375))
    pg.display.update()
    clock.tick(60)

pg.quit()
