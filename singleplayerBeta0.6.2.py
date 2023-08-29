import pygame as pg
import sys, random
import noise

class Character:
  def __init__(self, posX, posY, vX, vY ,health, stamina, defence, dmg, W, H, skinL, skinD , isInAir, isOnIce, isInWater, isFlying, isSing, o2):
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
    self.skinL = skinL
    self.skinD = skinD
    self.isOnice = isOnIce
    self.isInWater = isInWater
    self.isFlying = isFlying
    self.isSing = isSing
    self.o2 = o2
pg.init()

screen = pg.display.set_mode((1280, 800))
clock = pg.time.Clock()
    # Create the character
character = Character(1000, 450, 0, 0, 100, 100, 10, 10, 32, 64, "playerL.png", "playerD.png", True, False, False, False, False, 0)
    # Create the ground
ground = pg.Rect(0, 500, 800, 100)
    # Main game loop
 
yd = 0

world = [[0 for i in range(200)] for i in range(200)]

startx = random.randint(1,10000)
for x, tile in enumerate(world[0]):
    # noise1(x, octaves=1, persistence=0.5, lacunarity=2.0, repeat=1024, base=0.0)
    gen = noise.pnoise1(x * 0.1 + startx, repeat=999999999, persistence=0.1)
    if gen >= 0: 
        for i in range(int(gen * 10) + 125,200): world[i][x] = 1
    elif gen < 0: 
        for i in range(0-int(gen * 10) + 125,200): world[i][x] = 1
Block_Dict = {
    0 : {"block_name" : "Air" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 1000, "texture" : "null" , "walk_sound" : "null", "break_sound" : "null"},
    2 : {"block_name" : "Dirt" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load(".\\dirt.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"},
    1 : {"block_name" : "Stone" , "breaking_time" : 180 , "breaking_tool" : "pickaxe", "hardness" : 1, "texture" : pg.image.load(".\\stone.png").convert() , "walk_sound" : "stonewalk.ogg", "break_sound" : "stonebreak.ogg"},
    3 : {"block_name" : "Bedrok" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 6969, "texture" : pg.image.load(".\\Bedrock.png").convert() , "walk_sound" : "bedrock.ogg", "break_sound" : "null"},
    4 :  {"block_name" : "Grass" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load(".\\grass.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg",},
    5: {"block_name" : "Wood" , "breaking_time" : 120 , "breaking_tool" : "axe", "hardness" : 1, "texture" : pg.image.load(".\\wood.png").convert(), "walk_sound" : "woodwalk.ogg", "break_sound" : "woodbreak.ogg"},
    6: {"block_name" : "Leaves" , "breaking_time" : 30 , "breaking_tool" : "null", "hardness" : 1, "texture" :pg.image.load(".\\leaves.png").convert() , "walk_sound" : "leaveswalk.ogg", "break_sound" : "leavesbreak.ogg"}}



poruke=["","","","",""]
user_text = ''
a = False
w = 280
font = pg.font.Font(None, 32)

screen.fill("blue")
charl = pg.image.load(".\\character_l.png")
charl= pg.transform.scale(charl, (32,86))
chard = pg.image.load(".\\character_d.png")
chard= pg.transform.scale(chard, (32,86))
LastClick = 1

#---INVENTORY-----
font1 = pg.font.SysFont('Comic Sans MS', 25, bold=pg.font.Font.bold)
slot = 1
H = 850
XX = (1280 - 620) / 2
L = [Block_Dict[1]["texture"], Block_Dict[2]["texture"], Block_Dict[4]["texture"], Block_Dict[5]["texture"], Block_Dict[6]["texture"], 0,0,0, 0]
LB = [1, 1, 1, 1, 1, 0, 0, 0, 0]


#-----INVENTORY-----#
#DRAW
def draw(menjansvet, daynightcycle):
    global slot, W, H, L, LB, font1
    (daynightcycle)
    screen.fill((0,120*daynightcycle//25000,255*daynightcycle//25000))
    # yd -= 1
    # pg.draw.rect(screen, "white", ground)
    
    u = max((character.posY-screen.get_height()//2)//32,0)
    d = max((character.posY+screen.get_height()//2)//32,0)
    l = max((character.posX-screen.get_width()//2)//32,0)
    r = max((character.posX+screen.get_width()//2)//32,0)
    d +=1
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
                world[21][100] = 1
                imp = Block_Dict[world[y][x]]["texture"]    
                screen.blit(imp,(cnt2*32,cnt1 *32))
    if LastClick == 1:
        screen.blit(chard,(screen.get_width()//2-32, screen.get_height()//2-24, character.W, character.H)) #HARDCODE
    else:
        screen.blit(charl,(screen.get_width()//2-32, screen.get_height()//2-24,character.W, character.H)) #HARDCODE


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
 

displayPX, displayPY = screen.get_width()//2-32, screen.get_height()//2-16            
# EROZIJA
nesusedni = -1
for x in range(200):
    counter = 0
    nesusedni+=1
    for y in range (200):
        if world[y][x] == 1 and counter == 0:
            world[y][x] = 4
            counter = counter+1
            if(random.randint(1,5) == 1 and nesusedni >5 and x>2 and x < 198 and y>6):
                world[y-1][x] = 5
                world[y-2][x] = 5
                world[y-3][x] = 5
                world[y-4][x] = 5
                world[y-5][x] = 5
                world[y-6][x] = 6
                world[y-6][x+1] = 6
                world[y-6][x-1] = 6
                world[y-5][x-1] = 6
                world[y-5][x+1] = 6
                world[y-5][x-2] = 6
                world[y-5][x+2] = 6
                world[y-4][x+1] = 6
                world[y-4][x+2] = 6
                world[y-4][x-1] = 6
                world[y-4][x-2] = 6
                nesusedni = 0
        elif world[y][x] == 1 and counter < 3:
            world[y][x] = 2
            counter = counter +1
        if y<= screen.get_height()//64:
            world[y][x] = 3
        if y>= 200- screen.get_height()//64:
            world[y][x] = 3
selectedBlock=1
framecounter = 0
daynightcycle = 25000
draw(True,0)
while True:
        if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[0] >= 15 and pg.mouse.get_pos()[0] <= 280 and pg.mouse.get_pos()[1] >= 155 and pg.mouse.get_pos()[1] <= 185):
            a = True
        if daynightcycle == 0:
            spusta = False
        framecounter = framecounter%100+1
        if daynightcycle <25000 and not spusta:
            daynightcycle+=1
        else:
            spusta = True
            daynightcycle -= 1
        # dt = clock.tick(60) / 1000
        character.isInAir = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and a:
                if event.key == pg.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pg.K_RETURN:
                    poruke.append(user_text)
                
                    user_text = ''
                    a = False
                else:
                    user_text += event.unicode
            if event.type == pg.MOUSEWHEEL:
                if event.y > 0:
                    slot += 1
                if event.y < 0:
                    slot -= 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    slot = 1
                    selectedBlock = 1
                if event.key == pg.K_2:
                    slot = 2
                    selectedBlock = 2
                if event.key == pg.K_3:
                    slot = 3
                    selectedBlock = 4
                if event.key == pg.K_4:
                    slot = 4
                    selectedBlock = 5
                if event.key == pg.K_5:
                    slot = 5
                    selectedBlock = 6
                if event.key == pg.K_6:
                    slot = 6
                    selectedBlock = 0
                if event.key == pg.K_7:
                    slot = 7
                    selectedBlock = 0
                if event.key == pg.K_8:
                    slot = 8
                    selectedBlock = 0
                if event.key == pg.K_9:
                    slot = 9
                    selectedBlock = 0
                if event.key == pg.K_a:
                    LastClick = 0
                if event.key == pg.K_d:
                    LastClick = 1
            
                
            
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
                        if world[int(character.posY-character.H/2)//32-1][(character.posX-character.W//2)//32] >0:
                            character.vY = 0
                            character.isInAir = True
                            
                    else:   
                        if world[int(character.posY+character.H/2-character.posY%32)//32][(character.posX-character.W//2)//32] >0:
                            character.posY -= character.posY%32
                            character.isInAir = False
                        if world[int(character.posY+character.H/2-character.posY%32)//32-1][(character.posX-character.W//2)//32] >0:
                            character.posY -= 32
                            character.isInAir = False
                        if world[int(character.posY-character.H/2-character.posY%32)//32][(character.posX-character.W//2)//32] >0:
                            character.vY = 0
                            character.isInAir = True
                
        keys = pg.key.get_pressed()
        menjansvet = True
        if pg.mouse.get_pressed()[2]:
                    if pg.mouse.get_pos()[0] > displayPX + character.W:
                        if pg.mouse.get_pos()[1] < displayPY and world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2+32)//32] ==0:
                            world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2+32)//32] =selectedBlock
                        elif pg.mouse.get_pos()[1]<displayPY+32  and world[int(character.posY-character.H/2)//32][(character.posX-character.W//2+32)//32] ==0: 
                            world[int(character.posY-character.H/2)//32][(character.posX-character.W//2+32)//32] =selectedBlock
                        elif pg.mouse.get_pos()[1]<displayPY+64  and world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2+32)//32] ==0: 
                            world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2+32)//32] =selectedBlock
                        elif  world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2+32)//32] ==0: 
                            world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2+32)//32] =selectedBlock
                    elif pg.mouse.get_pos()[0] > displayPX :
                        if pg.mouse.get_pos()[1] < displayPY and world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2)//32] ==0:
                            world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2)//32] = selectedBlock
                
                        elif  pg.mouse.get_pos()[1] > displayPY+32 and world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2)//32] ==0: 
                            world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2)//32] =selectedBlock
                    else: 
                        if pg.mouse.get_pos()[1] < displayPY and world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2-32)//32] ==0:
                            world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2-32)//32] = selectedBlock
                        elif pg.mouse.get_pos()[1]<displayPY+32  and world[int(character.posY-character.H/2)//32][(character.posX-character.W//2-32)//32] ==0: 
                            world[int(character.posY-character.H/2)//32][(character.posX-character.W//2-32)//32] =selectedBlock
                        elif pg.mouse.get_pos()[1]<displayPY+64  and world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2-32)//32] ==0: 
                            world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2-32)//32] =selectedBlock
                        elif  world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2-32)//32] ==0: 
                            world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2-32)//32] =selectedBlock 
        if pg.mouse.get_pressed()[0]:
                    if pg.mouse.get_pos()[0] > displayPX + character.W:
                        if pg.mouse.get_pos()[1] < displayPY and world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2+32)//32] !=3:
                            world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2+32)//32] = 0
                        elif pg.mouse.get_pos()[1]<displayPY+32  and world[int(character.posY-character.H/2)//32][(character.posX-character.W//2+32)//32] !=3: 
                            world[int(character.posY-character.H/2)//32][(character.posX-character.W//2+32)//32] =0
                        elif pg.mouse.get_pos()[1]<displayPY+64  and world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2+32)//32] !=3: 
                            world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2+32)//32] =0
                        elif  world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2+32)//32] !=3: 
                            world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2+32)//32] =0
                    elif pg.mouse.get_pos()[0] > displayPX :
                        if pg.mouse.get_pos()[1] < displayPY and world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2)//32] !=3:
                            world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2)//32] = 0
                
                        elif  pg.mouse.get_pos()[1] > displayPY+32 and world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2)//32] !=3: 
                            world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2)//32] =0
                    else: 
                        if pg.mouse.get_pos()[1] < displayPY and world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2-32)//32] !=3:
                            world[int(character.posY-character.H/2-32)//32][(character.posX-character.W//2-32)//32] = 0
                        elif pg.mouse.get_pos()[1]<displayPY+32  and world[int(character.posY-character.H/2)//32][(character.posX-character.W//2-32)//32] !=3: 
                            world[int(character.posY-character.H/2)//32][(character.posX-character.W//2-32)//32] =0
                        elif pg.mouse.get_pos()[1]<displayPY+64  and world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2-32)//32] !=3: 
                            world[int(character.posY-character.H/2+32)//32][(character.posX-character.W//2-32)//32] =0
                        elif  world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2-32)//32] !=3: 
                            world[int(character.posY-character.H/2+64)//32][(character.posX-character.W//2-32)//32] =0
        if character.posX>= 5600:
            mozeDesno = False
        if character.posX <= 800:
            mozeLevo = False 
        if a:
            mozeLevo = False
            mozeDesno = False
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
            

        
        menjansvet = False
        draw(True,daynightcycle)
        pg.draw.rect(screen, "Black", (0, 0, 300, 190))
        pg.draw.rect(screen, "Gray", (10, 155, w, 30))
        text_surface = font.render(user_text, True, (0, 0, 0))
        text_surface1 = font.render(poruke[-1], True, (255, 255, 255))
        text_surface2 = font.render(poruke[-2], True, (255, 255, 255))
        text_surface3 = font.render(poruke[-3], True, (255, 255, 255))
        text_surface4 = font.render(poruke[-4], True, (255, 255, 255))
        text_surface5 = font.render(poruke[-5], True, (255, 255, 255))
        screen.blit(text_surface, (15, 160))
        screen.blit(text_surface1, (15, 130))
        screen.blit(text_surface2, (15, 100))
        screen.blit(text_surface3, (15, 70))
        screen.blit(text_surface4, (15, 40))
        screen.blit(text_surface5, (15, 10))
        w = max(280, text_surface.get_width() + 10)
        
        pg.display.update()
        clock.tick(100)
