import pygame as pg
import sys, random
import noise

W = 1280
H = 800

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

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
    # Create the character
character = Character(1000, 250, 0, 0, 100, 100, 10, 10, 32, 64, "player.png", True, False, False, False, False, 0)
    # Create the ground
ground = pg.Rect(0, 500, 800, 100)
    # Main game loop

#-----INVENTORY-----#
font1 = pg.font.SysFont('Comic Sans MS', 25, bold=pg.font.Font.bold)
slot = 1
XX = (W - 620) / 2
#DODAJTE SLIKE DOLE
image = pg.image.load("C:\\Users\\korisnik\\Downloads\\BlueCube.png").convert()
image1 = pg.image.load("C:\\Users\\korisnik\\Downloads\\RedCube.png").convert()
dirt = pg.image.load(".\\dirt.png")
stone = pg.image.load(".\\stone.png")
grass = pg.image.load(".\\grass.png")
L = [stone, dirt, grass, stone, dirt, grass, image1, image, 0]
LB = [1, 2, 3, 4, 5, 6, 7, 8, 0]
#-----INVENTORY-----#
 
yd = 0

world = [[0 for i in range(200)] for i in range(200)]

startx = random.randint(1,10000)
for x, tile in enumerate(world[0]):
    # noise1(x, octaves=1, persistence=0.5, lacunarity=2.0, repeat=1024, base=0.0)
    gen = noise.pnoise1(x * 0.1 + startx, repeat=999999999, persistence=0.1)
    if gen >= 0: 
        for i in range(int(gen * 10) + 25,200): world[i][x] = 1
    elif gen < 0: 
        for i in range(0-int(gen * 10) + 25,200): world[i][x] = 1
Block_Dict = {
    0 : {"block_name" : "Air" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 1000, "texture" : "null" , "walk_sound" : "null", "break_sound" : "null"},
    2 : {"block_name" : "Dirt" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load(".\\dirt.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"},
    1 : {"block_name" : "Stone" , "breaking_time" : 120 , "breaking_tool" : "pickaxe", "hardness" : 1, "texture" : pg.image.load(".\\stone.png").convert() , "walk_sound" : "stonewalk.ogg", "break_sound" : "stonebreak.ogg"},
    3 : {"block_name" : "Bedrok" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 6969, "texture" : "bedrock.png" , "walk_sound" : "bedrock.ogg", "break_sound" : "null"},
    4 :  {"block_name" : "Grass" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load(".\\grass.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"}
}
screen.fill("blue")
def draw(menjansvet):
    global slot, W, H, L, LB, font1
    
    screen.fill("blue")
    # yd -= 1
    # pg.draw.rect(screen, "white", ground)
    
    u = max((character.posY-screen.get_height()//2)//32,0)
    d = max((character.posY+screen.get_height()//2)//32,0)
    l = max((character.posX-screen.get_width()//2)//32,0)
    r = max((character.posX+screen.get_width()//2)//32,0)
    d +=1
    print(u,d,l,r)
    cnt1 = -1
    cnt2 = -1
    if menjansvet:
        for y in range(u,d):
            cnt1 += 1
            cnt2 =-1  
            for x in range(l,r):
                cnt2 += 1
                if world[y][x] == 0:
                    continue
                imp = Block_Dict[world[y][x]]["texture"]    
                screen.blit(imp,(cnt2*32,cnt1 *32))

    #-----INVENTORY-----#
    if slot < 1:
        slot = 9
    if slot > 9:
        slot = 1
    pg.draw.rect(screen, "Black", (XX - 25,  H - 150, 670, 110))
    if (slot == 1):
        pg.draw.rect(screen, "Gold", (XX - 5,  H - 130, 70, 70))
    elif (slot == 2):
        pg.draw.rect(screen, "Gold", (XX + 70 - 5,  H - 130, 70, 70))
    elif (slot == 3):
        pg.draw.rect(screen, "Gold", (XX + 70 * 2 - 5,  H - 130, 70, 70))
    elif (slot == 4):
        pg.draw.rect(screen, "Gold", (XX + 70 * 3 - 5,  H - 130, 70, 70))
    elif (slot == 5):
        pg.draw.rect(screen, "Gold", (XX + 70 * 4 - 5,  H - 130, 70, 70))
    elif (slot == 6):
        pg.draw.rect(screen, "Gold", (XX + 70 * 5 - 5,  H - 130, 70, 70))
    elif (slot == 7):
        pg.draw.rect(screen, "Gold", (XX + 70 * 6 - 5,  H - 130, 70, 70))
    elif (slot == 8):
        pg.draw.rect(screen, "Gold", (XX + 70 * 7 - 5,  H - 130, 70, 70))
    elif (slot == 9):
        pg.draw.rect(screen, "Gold", (XX + 70 * 8 - 5,  H - 130, 70, 70))
    pg.draw.rect(screen, "Gray", (XX,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 2,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 3,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 4,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 5,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 6,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 7,  H - 125, 60, 60))
    pg.draw.rect(screen, "Gray", (XX + 70 * 8,  H - 125, 60, 60))
    if (L[0] != 0):
        screen.blit(L[0], (XX + 5,  H - 120))
        img1 = font1.render(str(int(LB[0])), True, 'Black')
        if LB[0] < 10:
            screen.blit(img1, (XX + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 30,  H - 95))
    if (L[1] != 0):
        screen.blit(L[1], (XX + 75,  H - 120))
        img1 = font1.render(str(int(LB[1])), True, 'Black')
        if LB[1] < 10:
            screen.blit(img1, (XX + 70 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 + 30,  H - 95))
    if (L[2] != 0):
        screen.blit(L[2], (XX + 70 * 2 + 5,  H - 120))
        img1 = font1.render(str(int(LB[2])), True, 'Black')
        if LB[2] < 10:
            screen.blit(img1, (XX + 70 * 2 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 2 + 30,  H - 95))
    if (L[3] != 0):
        screen.blit(L[3], (XX + 70 * 3 + 5,  H - 120))
        img1 = font1.render(str(int(LB[3])), True, 'Black')
        if LB[3] < 10:
            screen.blit(img1, (XX + 70 * 3 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 3 + 30,  H - 95))
    if (L[4] != 0):
        screen.blit(L[4], (XX + 70 * 4 + 5,  H - 120))
        img1 = font1.render(str(int(LB[4])), True, 'Black')
        if LB[4] < 10:
            screen.blit(img1, (XX + 70 * 4 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 4 + 30,  H - 95))
    if (L[5] != 0):
        screen.blit(L[5], (XX + 70 * 5 + 5,  H - 120))
        img1 = font1.render(str(int(LB[5])), True, 'Black')
        if LB[5] < 10:
            screen.blit(img1, (XX + 70 * 5 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 5 + 30,  H - 95))
    if (L[6] != 0):
        screen.blit(L[6], (XX + 70 * 6 + 5,  H - 120))
        img1 = font1.render(str(int(LB[6])), True, 'Black')
        if LB[6] < 10:
            screen.blit(img1, (XX + 70 * 6 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 6 + 30,  H - 95))
    if (L[7] != 0):
        screen.blit(L[7], (XX + 70 * 7 + 5,  H - 120))
        img1 = font1.render(str(int(LB[7])), True, 'Black')
        if LB[7] < 10:
            screen.blit(img1, (XX + 70 * 7 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 7 + 30,  H - 95))
    if (L[8] != 0):
        screen.blit(L[8], (XX + 70 * 8 + 5,  H - 120))
        img1 = font1.render(str(int(LB[8])), True, 'Black')
        if LB[8] < 10:
            screen.blit(img1, (XX + 70 * 8 + 40,  H - 95))
        else:
            screen.blit(img1, (XX + 70 * 8 + 30,  H - 95))
   #-----INVENTORY-----#
                        
                
                
                
    pg.draw.rect(screen, "red", (screen.get_width()//2-32, screen.get_height()//2-15            ,character.W, character.H))
    pg.display.flip()
 


# EROZIJA
for x in range(200):
    counter = 0
    for y in range (200):
        if world[y][x] == 1 and counter == 0:
            world[y][x] = 4
            counter = counter+1
        elif world[y][x] == 1 and counter < 3:
            world[y][x] = 2
            counter = counter +1
framecounter = 0
draw(True)
while True:
        framecounter = framecounter%100+1
        # dt = clock.tick(60) / 1000
        character.isInAir = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEWHEEL:
                if event.y > 0:
                    slot += 1
                if event.y < 0:
                    slot -= 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    slot = 1
                if event.key == pg.K_2:
                    slot = 2
                if event.key == pg.K_3:
                    slot = 3
                if event.key == pg.K_4:
                    slot = 4
                if event.key == pg.K_5:
                    slot = 5
                if event.key == pg.K_6:
                    slot = 6
                if event.key == pg.K_7:
                    slot = 7
                if event.key == pg.K_8:
                    slot = 8
                if event.key == pg.K_9:
                    slot = 9
        mozeDesno = True
        mozeLevo = True
        if character.isInAir == False:
                    if (character.posY+character.H/2 )%32 ==0:
                        if world[int(character.posY+character.H/2)//32][(character.posX-character.W//2)//32-1] >0:
                            character.isInAir = False
                        else:
                            character.isInAir=True
                    else:   
                            if world[int(character.posY+character.H/2)//32][(character.posX-character.W//2)//32] >0:
                                character.posY -= character.posY%32
                                character.isInAir = False
                    if world[int(character.posY+character.H/2-1)//32][(character.posX-character.W//2)//32] > 0: #dolelevo
                        mozeLevo = False                        
                    if world[int(character.posY-character.H/2)//32][(character.posX-character.W//2)//32] >0: #gorelevo
                        mozeLevo = False                        
                    if world[int(character.posY+character.H/2-1)//32][(character.posX-character.W//2)//32+2] > 0:
                        mozeDesno = False                        
                    if world[int(character.posY-character.H/2)//32][(character.posX-character.W//2)//32+2] >0:
                        mozeDesno = False                        
                        
                    
        else:
                    if world[int(character.posY-character.posY%32-character.H/2)//32][(character.posX-character.W//2)//32-1] > 0: #dolelevo
                        mozeLevo = False                        
                    if world[int(character.posY-character.posY%32+32-character.H/2)//32][(character.posX-character.W//2)//32-1] >0: #gorelevo
                        mozeLevo = False                        
                    if world[int(character.posY-character.posY%32-character.H/2)//32][(character.posX-character.W//2)//32+1] > 0:
                        mozeDesno = False                        
                    if world[int(character.posY-character.posY%32+32-character.H/2)//32][(character.posX-character.W//2)//32+1] >0:
                        mozeDesno = False                        
                        
                    if (character.posY+character.H/2 )%32 ==0:
                        if world[int(character.posY+character.H/2)//32][(character.posX-character.W//2)//32] >0:
                            character.isInAir = False
                    else:   
                        if world[int(character.posY+character.H/2-character.posY%32)//32][(character.posX-character.W//2)//32] >0:
                            character.posY -= character.posY%32
                            character.isInAir = False
                        if world[int(character.posY+character.H/2-character.posY%32)//32-1][(character.posX-character.W//2)//32] >0:
                            character.posY -= 32
                            character.isInAir = False
                
        keys = pg.key.get_pressed()
        if character.posX>= 5600:
            mozeDesno = False
        if character.posX <= 800:
            mozeLevo = False 
        
        if keys[pg.K_a] and mozeLevo and framecounter%8==0:
            character.posX -= 32
        if keys[pg.K_d] and mozeDesno and framecounter%8==0:
            character.posX += 32   
        if not character.isInAir:
            character.vY = 0
        if keys[pg.K_SPACE] and character.isInAir == False:
            character.vY -= 16
            character.isInAir = True
        if character.isInAir :
            character.vY +=1
        else:
            character.vY = 0
        character.posY += character.vY
        

        #KOD ZA RAZBIJANJE BLOKOVA
        # menjansvet = true
        #else
        
        menjansvet = False
        draw(True)

        clock.tick(100)
