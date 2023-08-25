import pygame as pg
pg.init()
 

clock = pg.time.Clock()

HEIGHT=640
WIDTH=480
running=True

screen = pg.display.set_mode((WIDTH, HEIGHT))

#sve za pravougaonik
rect_w=50
rect_h=50
x_move=5
x=WIDTH/2-rect_w/2
y=HEIGHT/2-rect_h/2


def draw(iks, ipsilon):
    screen.fill("white")

    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        iks-=10

    if keys[pg.K_d]:
        iks+=10

    if keys[pg.K_w]:
        ipsilon-=10

    if keys[pg.K_s]:
        ipsilon+=10

    x=iks
    y=ipsilon
    pg.draw.rect(screen, "blue", (iks,ipsilon, rect_w, rect_h))
    pg.display.update()
    return x,y  


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
    
    x,y=draw(x,y)

    clock.tick(60)
    pg.display.flip()
    pg.display.update
pg.quit()
