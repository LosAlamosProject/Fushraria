import pygame as pg
import sys, random
import noise
import math

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
poruke=["","","","",""]
user_text = ''
screen = pg.display.set_mode((1280, 800))
clock = pg.time.Clock()
    # Create the character
character = Character(1000, 250, 0, 0, 100, 100, 10, 10, 32, 64, "player.png", True, False, False, False, False, 0)
    # Create the ground
ground = pg.Rect(0, 500, 800, 100)
    # Main game loop
 
yd = 0

world = [[0 for i in range(200)] for i in range(200)]

a=False
font = pg.font.Font(None, 32)
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
def draw(menjansvet, daynightcycle):
    print(daynightcycle)
    screen.fill((0,120*daynightcycle//25000,255*daynightcycle//25000))
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
        
                        
                
                
                
    pg.draw.rect(screen, "red", (screen.get_width()//2-32, screen.get_height()//2-15            ,character.W, character.H))
 
w = 280

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
daynightcycle = 0
draw(True,0)
running = True
while running:
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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and a:
                if event.key == pg.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pg.K_RETURN:
                    poruke.append(user_text)
                
                    user_text = ''
                    a = False
                else:
                    user_text += event.unicode
        if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[0] >= 15 and pg.mouse.get_pos()[0] <= 280 and pg.mouse.get_pos()[1] >= 155 and pg.mouse.get_pos()[1] <= 185):
            a = True

        
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
        pg.display.flip()
        clock.tick(10000)
pg.quit()
