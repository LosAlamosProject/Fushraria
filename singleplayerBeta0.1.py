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
character = Character(224, 250, 0, 0, 100, 100, 10, 10, 32, 64, "player.png", True, False, False, False, False, 0)
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
Block_Dict = {
    0 : {"block_name" : "Air" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 1000, "texture" : pg.image.load("C:\\Users\\korisnik\\Desktop\\filikili\\air.png").convert() , "walk_sound" : "null", "break_sound" : "null"},
    2 : {"block_name" : "Dirt" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load("C:\\Users\\korisnik\\Desktop\\filikili\\dirt.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"},
    1 : {"block_name" : "Stone" , "breaking_time" : 120 , "breaking_tool" : "pickaxe", "hardness" : 1, "texture" : pg.image.load("C:\\Users\\korisnik\\Desktop\\filikili\\stone.png").convert() , "walk_sound" : "stonewalk.ogg", "break_sound" : "stonebreak.ogg"},
    3 : {"block_name" : "Bedrok" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 6969, "texture" : "bedrock.png" , "walk_sound" : "bedrock.ogg", "break_sound" : "null"},
    4 :  {"block_name" : "Grass" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load("C:\\Users\\korisnik\\Desktop\\filikili\\grass.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"}
}
def draw(menjansvet):
    
    screen.fill("black")
    # yd -= 1
    # pg.draw.rect(screen, "white", ground)
    

    

    if menjansvet:
        for y, row in enumerate(world):
            for x, tile in enumerate(row):
                    imp = Block_Dict[tile]["texture"]
                    screen.blit(imp,(x*32,y*32))
    pg.draw.rect(screen, "red", (character.posX-character.W/2, character.posY-character.H/2, character.W, character.H))
    pg.display.flip()
 


# EROZIJA
for x in range(100):
    counter = 0
    for y in range (100):
        if world[y][x] == 1 and counter == 0:
            world[y][x] = 4
            counter = counter+1
        elif world[y][x] == 1 and counter < 3:
            world[y][x] = 2
            counter = counter +1

draw(True)
while True:
        character.isInAir = True
        # dt = clock.tick(60) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        mozeDesno = True
        mozeLevo = True
        if (character.posX-character.W/2) % 32 != 0:
            if world[int(character.posY+character.H/2)//32][int(character.posX-character.W/2)//32] >0:
                character.posY -= character.posY %32
                character.isInAir = False
            if world[int(character.posY+character.H/2)//32][int(character.posX-character.W/2)//32+1] >0:
                character.posY -= character.posY %32
                character.isInAir = False
        else:
            if world[int(character.posY+character.H/2-1)//32][(character.posX-character.W//2)//32-1] > 0:
                mozeLevo = False
            if world[int(character.posY-character.H/2)//32][(character.posX-character.W//2)//32-1] >0:
                mozeLevo=False
            if world[int(character.posY+character.H/2-1)//32][(character.posX-character.W//2)//32+1] > 0:
                mozeDesno = False
            if world[int(character.posY-character.H/2)//32][(character.posX-character.W//2)//32+1] >0:
                mozeDesno=False
            if world[int(character.posY+character.H/2-1)//32][(character.posX-character.W//2)//32-1] > 0:
                mozeLevo = False
            if (character.posY+character.H/2 %32) ==0:
                if world[int(character.posY+character.H/2+1)//32+1][(character. posX-character.W//2)//32] >0:
                    character.posY -= character.posY %32
                    character.isInAir=False
            else:
                if world[int(character.posY+character.H/2)//32][(character. posX-character.W//2)//32] >0:
                    character.isInAir=False
        keys = pg.key.get_pressed()
        print(mozeLevo, mozeDesno, character.isInAir)
        if keys[pg.K_a] and mozeLevo:
            character.posX -= 4
        if keys[pg.K_d] and mozeDesno:
            character.posX += 4
        if not character.isInAir:
            character.vY = 0
        if keys[pg.K_SPACE] and character.isInAir == False:
            character.vY -= 16
            character.isInAir = True
        if character.isInAir:
            character.vY +=1
        else:
            character.vY = 0
        character.posY += character.vY
        print(character.posX, character.posY)

        #KOD ZA RAZBIJANJE BLOKOVA
        # menjansvet = true
        #else
        menjansvet = False
        draw(True)

        clock.tick(60)
