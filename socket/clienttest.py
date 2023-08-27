import pygame as pg

pg.init()
from network import Network
import json
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()

screen.fill((255, 255, 255))
pg.display.update()

n = Network()
podaci=json.loads(n.pos.decode())
id=podaci.get("id")
world=podaci.get("world")
ball=pg.draw.circle(screen,(255, 0, 0),(400, 400), 50)
poze=[]
ball_x = 400
ball_y = 400

while True:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            
            pg.quit()
            exit()
    #make wasd movement without events
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        ball_x -= 5
    if keys[pg.K_d]:
        ball_x += 5
    if keys[pg.K_w]:
        ball_y -= 5
    if keys[pg.K_s]:
        ball_y += 5
    ball=pg.draw.circle(screen,(255, 0, 0),(ball_x,ball_y), 50)
    data=json.loads(n.send(json.dumps({"poz":[ball_x,ball_y,"",id],"world":world})).decode())
    poze=data.get("poz")
    world=data.get("world")
    for i in poze:
        if i[3]!=id:
            pg.draw.circle(screen,(255, 0, 0),(i[0],i[1]), 50)
    print(json.dumps([ball_x,ball_y]))
    pg.display.update()
    clock.tick(30)
        
