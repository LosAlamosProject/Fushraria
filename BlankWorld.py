import pygame as pg
import sys, random
import noise

class Character:
  def __init__(self, posX, posY, vX, vY ,health, stamina, defence, dmg, W, H, skin,  isInAir, isOnIce, isInWater, isFlying, isSprinting, o2):
    self.posX = posX
    self.posY = posY
    self.vX = vX
    self.vY = vY
    self.W = W
    self.H = H
    self.health = health
    self.stamina = stamina
    self.defence = defence
    self.dmg = dmg
    self.isInAir = isInAir
    self.skin = skin
    self.isOnice = isOnIce
    self.isInWater = isInWater
    self.isFlying = isFlying
    self.isSprinting = isSprinting
    self.o2 = o2
pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
    # Create the character
character = Character(100, 250, 0, 0, 100, 100, 10, 10, 50, 100, "player.png", True, False, False, False, False, 0)
    # Create the ground
ground = pg.Rect(0, 500, 800, 100)
    # Main game loop
 
yd = 0

world = [[0 for i in range(100)] for i in range(100)]

startx = random.randint(1,10000)
for x, tile in enumerate(world[0]):
    gen = noise.pnoise1(x * 0.1 + startx, repeat=999999999)
    if gen >= 0: 
        for i in range(int(gen * 10) + 10,100): world[i][x] = 1
    elif gen < 0: 
        for i in range(0-int(gen * 10) + 10,100): world[i][x] = 1

def draw():
    global yd
    screen.fill("black")
    # yd -= 1
    # pg.draw.rect(screen, "white", ground)
    pg.draw.rect(screen, "red", (character.posX-character.W/2, character.posY-character.H/2, character.W, character.H))

    


    for y, row in enumerate(world):
        for x, tile in enumerate(row):
            
            if tile == 1:
                pg.draw.rect(screen,(255,255,255),(x*32,y*32-yd,32,32))

    pg.display.flip()
 


# generated = noisegenerator.generate(100)
# for x, i in enumerate(generated):
#     if i > 0:
#         for y in range(int(i) * 3,99):
#             world[int(y)][x] = 1
#     else:
#         for y in range(int(-i) * 3,99):
#             world[int(y)][x] = 1

velocityX = 0
velocityY = 0
while True:
        # dt = clock.tick(60) / 1000

        character.posX += velocityX

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        if character.posY >= ground.top - character.H/2:
            character.isInAir = False
            velocityY = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            velocityX = -5 #PLAYER.SPEED
        elif keys[pg.K_d]:
            velocityX = 5 #PLAYER>SPEED
        else:
            velocityX = 0
        if keys[pg.K_SPACE] and character.isInAir == False:
            velocityY -= 15 #PLAYER.JUMPHEIGHT
            character.isInAir = True
        velocityY += 1 #GRAVITY
 
        if character.isInAir == True:
            character.posY += velocityY
        # Update the character's position
        draw()

        clock.tick(60)
