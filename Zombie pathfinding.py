import pygame as pg
import math
pg.init()
 

clock = pg.time.Clock()

HEIGHT=1920
WIDTH=1080
running=True

screen = pg.display.set_mode((WIDTH, HEIGHT))

#sve za pravougaonik/kvadrat

rect_w=32
rect_h=64
x=WIDTH/2-rect_w/2
y=HEIGHT/2-rect_h/2

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
    screen.fill("white")
    
    #uzima poziciju misa, zameni sa poz lika
    posX,posY=pg.mouse.get_pos() 


    #pomera zombija ka igracu
    if x < posX:
        x=x+16
    if x > posX:
        x=x-16

    #crta zombija
    pg.draw.rect(screen, "red", (x,y, rect_w, rect_h))
    pg.display.update()


    
    clock.tick(60)
    pg.display.flip()
    pg.display.update
pg.quit()