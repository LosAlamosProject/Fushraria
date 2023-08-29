import pygame as pg
import math
import random
pg.init()
 

clock = pg.time.Clock()

HEIGHT=500
WIDTH=1080
running=True

screen = pg.display.set_mode((WIDTH, HEIGHT))

#sve za pravougaonik/kvadrat

class Zombie:
    def __init__(self, zomb_w, zomb_h, zomb_x, zomb_y, health):
        self.zomb_w = zomb_w
        self.zomb_h = zomb_h
        self.zomb_x = zomb_x
        self.zomb_y = zomb_y
        self.health = health
    def ZombieDraw(self):
        pg.draw.rect(screen, "red", (self.zomb_x, self.zomb_y, self.zomb_w, self.zomb_h))

zomb_w = 32
zomb_h = 64
zomb_x = WIDTH / 2- zomb_w / 2
zomb_y = HEIGHT / 2- zomb_h / 2
health = 100
ZT = 5000
ZTL = 5000
t = 10
LZ = []
LZPX = []
LZPY = []

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
    screen.fill("white")
    
    posX,posY=pg.mouse.get_pos()
    if ZTL <= 0:
        ZBX = random.randint(0, 300)
        ZPOM = random.randint(0, 1)
        if ZPOM == 0:
            if posX + ZBX > WIDTH - zomb_w:
                ZBX = WIDTH - zomb_w - posX
            Z = Zombie(zomb_w, zomb_h, posX + ZBX, zomb_y, health)
        else:
            if posX - ZBX < 0:
                ZBX = 0
            Z = Zombie(zomb_w, zomb_h, posX - ZBX, zomb_y, health)
        LZ.append(Z)
        LZPX.append(Z.zomb_x)
        ZTL = ZT
    else:
        ZTL -= t
    
    for i in range(len(LZ)):
        if LZ[i].zomb_x < posX and LZ[i].zomb_x + 4 not in LZPX:
            LZ[i].zomb_x += 4
        if LZ[i].zomb_x > posX and LZ[i].zomb_x - 4 not in LZPX:
            LZ[i].zomb_x -= 4
        LZPX[i] = LZ[i].zomb_x
    
    for i in range(len(LZ)):
        #pg.draw.rect(screen, "red", (LZ[i].zomb_x, LZ[i].zomb_y, LZ[i].zomb_w, LZ[i].zomb_h))
        LZ[i].ZombieDraw()
    print(LZPX)
    t = clock.tick(100)
    pg.display.update()
pg.quit()
