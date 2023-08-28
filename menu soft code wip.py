import pygame as pg
import sys, random
import noise

class Character:
  def __init__(self, posX, posY, vX, vY ,health, stamina, defence, dmg, W, H, skinL, skinD , isInAir, isOnIce, isInWater, isFlying, isSprinting, o2):
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
    self.isSprinting = isSprinting
    self.o2 = o2
pg.init()
WIDTH=1920
HEIGHT=1020

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
    # Create the character
character = Character(1000, 250, 0, 0, 100, 100, 10, 10, 32, 64, "playerL.png", "playerD.png", True, False, False, False, False, 0)
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
        for i in range(int(gen * 10) + 25,200): world[i][x] = 1
    elif gen < 0: 
        for i in range(0-int(gen * 10) + 25,200): world[i][x] = 1
Block_Dict = {
    0 : {"block_name" : "Air" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 1000, "texture" : "null" , "walk_sound" : "null", "break_sound" : "null"},
    2 : {"block_name" : "Dirt" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load(".\\dirt.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"},
    1 : {"block_name" : "Stone" , "breaking_time" : 180 , "breaking_tool" : "pickaxe", "hardness" : 1, "texture" : pg.image.load(".\\stone.png").convert() , "walk_sound" : "stonewalk.ogg", "break_sound" : "stonebreak.ogg"},
    3 : {"block_name" : "Bedrok" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 6969, "texture" : "bedrock.png" , "walk_sound" : "bedrock.ogg", "break_sound" : "null"},
    4 :  {"block_name" : "Grass" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : pg.image.load(".\\grass.png").convert() , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg",},
    5: {"block_name" : "Wood" , "breaking_time" : 120 , "breaking_tool" : "axe", "hardness" : 1, "texture" : pg.image.load(".\\wood.png").convert(), "walk_sound" : "woodwalk.ogg", "break_sound" : "woodbreak.ogg"},
    6: {"block_name" : "Leaves" , "breaking_time" : 30 , "breaking_tool" : "null", "hardness" : 1, "texture" :pg.image.load(".\\leaves.png").convert() , "walk_sound" : "leaveswalk.ogg", "break_sound" : "leavesbreak.ogg"}}



poruke=["","","","",""]
user_text = ''
a = False
w = 280
font = pg.font.Font(None, 32)

screen.fill("blue")
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
    #print(daynightcycle)
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
    pg.draw.rect(screen, "red", (screen.get_width()//2-32, screen.get_height()//2-15            ,character.W, character.H))


    #-----INVENTORY-----#
    if slot < 1:
        slot = 9
    if slot > 9:
        slot = 1
    
    
    

    duz_pravoug=670
    sir_pravoug=110
    kvadrat_a=70


    pg.draw.rect(screen, "Black", (WIDTH/2-duz_pravoug/2, HEIGHT-sir_pravoug, duz_pravoug, sir_pravoug))
    if (slot == 1):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a - 60,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 2):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 3):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 2 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 4):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 3 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 5):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 4 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 6):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 5 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 7):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 6 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 8):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 7 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    elif (slot == 9):
        pg.draw.rect(screen, "Gold", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 8 + 10,  HEIGHT - 90, kvadrat_a, kvadrat_a))
    
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 2 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 3 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 4 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 5 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 6 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 7 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))
    pg.draw.rect(screen, "Gray", (WIDTH/2-duz_pravoug/2 + kvadrat_a * 8 + 15,  HEIGHT - kvadrat_a - 15, 60, 60))


    if (L[0] != 0):
        screen.blit(L[0], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 0.5 - 5,  H - 130))
        img1 = font1.render(str(int(LB[0])), True, 'Black')
        LB[0]=1
        if LB[0] < 10:
            screen.blit(img1, (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a/2 + 5,  H - 105))
        else:
            screen.blit(img1, (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 0.5 - 2.5,  H - 105))

    if (L[1] != 0):
        screen.blit(L[1], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 1.5 - 5,  H - 120))
        img1 = font1.render(str(int(LB[1])), True, 'Black')
        if LB[1] < 10:
            screen.blit(img1, (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a/2 + 5,  H - 105))
        else:
            screen.blit(img1, (duz_pravoug + 70 + 30,  H - 105))

    if (L[2] != 0):
        screen.blit(L[2], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 2.5 - 5,  H - 105))
        img1 = font1.render(str(int(LB[2])), True, 'Black')
        if LB[2] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 2 + 40,  H - 105))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 2 + 30,  H - 105))

    if (L[3] != 0):
        screen.blit(L[3], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 3.5 - 5,  H - 105))
        img1 = font1.render(str(int(LB[3])), True, 'Black')
        if LB[3] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 3 + 40,  H - 105))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 3 + 30,  H - 105))

    if (L[4] != 0):
        screen.blit(L[4], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 4.5 - 5,  H - 105))
        img1 = font1.render(str(int(LB[4])), True, 'Black')
        if LB[4] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 4 + 40,  H - 105))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 4 + 30,  H - 105))

    if (L[5] != 0):
        screen.blit(L[5], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 5.5 - 5,  H - 120))
        img1 = font1.render(str(int(LB[5])), True, 'Black')
        if LB[5] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 5 + 40,  H - 105))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 5 + 30,  H - 95))
    if (L[6] != 0):
        screen.blit(L[6], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 6.5 - 5,  H - 120))
        img1 = font1.render(str(int(LB[6])), True, 'Black')
        if LB[6] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 6 + 40,  H - 95))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 6 + 30,  H - 95))

    if (L[7] != 0):
        screen.blit(L[7], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 7.5 - 5,  H - 120))
        img1 = font1.render(str(int(LB[7])), True, 'Black')
        if LB[7] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 7 + 40,  H - 95))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 7 + 30,  H - 95))

    if (L[8] != 0):
        screen.blit(L[8], (WIDTH / 2 - duz_pravoug / 2 + kvadrat_a * 8.5 - 5,  H - 120))
        img1 = font1.render(str(int(LB[8])), True, 'Black')
        if LB[8] < 10:
            screen.blit(img1, (duz_pravoug + 70 * 8 + 40,  H - 95))
        else:
            screen.blit(img1, (duz_pravoug + 70 * 8 + 30,  H - 95))
            
   #-----INVENTORY-----#
 


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
#print(world)
framecounter = 0
daynightcycle = 0
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
        

        #KOD ZA RAZBIJANJE BLOKOVA
        # menjansvet = true
        #else
        
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