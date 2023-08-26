import pygame as pg
import sys, random, math
import noise
#BLOCK SIZE 50 WORLD SIZE 100x100
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
screen = pg.display.set_mode((1280, 800))
clock = pg.time.Clock()
    # Create the character
character = Character(100, 250, 0, 0, 95, 45, 10, 10, 45, 96, "player.png", True, False, False, False, False, 0)



 
yd = 0
WORLDW =100
WORLDH = 100
world = [[0 for i in range(WORLDW)] for i in range(WORLDH)]

startx = random.randint(1,10000)
for x, tile in enumerate(world[0]):
    gen = noise.pnoise1(x * 0.1 + startx, repeat=999999)
    if gen >= 0: 
        for i in range(int(gen * 10) + 10,100): world[i][x] = 1
    elif gen < 0: 
        for i in range(0-int(gen * 10) + 10,100): world[i][x] = 1
print(world)
def draw():
    global yd
    screen.fill("black")
    pg.draw.rect(screen, "red", (character.posX-character.W/2, character.posY-character.H/2, character.W, character.H))

    


    for y, row in enumerate(world):
        for x, tile in enumerate(row):
            
            if tile == 1:
                pg.draw.rect(screen,(255,255,255),(x*50,y*50-yd,50,50))

    pg.display.flip()
 


velocityX = 0
velocityY = 0
while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            velocityX = -5 #PLAYER.SPEED
        elif keys[pg.K_d]:
            velocityX = 5 #PLAYER>SPEED
        else:
            velocityX = 0
        justjumped = False
        if keys[pg.K_SPACE] and character.isInAir == False:
            velocityY -= 20      #PLAYER.JUMPHEIGHT
            character.isInAir = True
            justjumped = True
        velocityY += 1 #GRAVITY
        print(math.floor((character.posX+character.W/2)/50), (character.posY+character.H//2)//50)
        if  world[(character.posY+character.H//2)//50][math.floor((character.posX+character.W/2)/50)] == 1:
            character.isInAir = False
        else:
            character.isInAir = True
        if character.isInAir == True or justjumped:
            character.posY += velocityY
        # Update the character's position
        character.posX += velocityX
        print(character.posX/50, character.posY/50)
        draw()

        clock.tick(60)
