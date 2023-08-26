import pygame as pg
import sys
import keyboard
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
character = Character(100, 450, 0, 0, 100, 100, 10, 10, 50, 100, "player.png", False, False, False, False, False, 0)
    # Create the ground
ground = pg.Rect(0, 500, 800, 100)
    # Main game loop
 
def draw():
    screen.fill("black")
    pg.draw.rect(screen, "white", ground)
    pg.draw.rect(screen, "red", (character.posX-character.W/2, character.posY-character.H/2, character.W, character.H))
    pg.display.update()
 
 
 
 
velocityY = 0
while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        if character.posY >= ground.top - character.H/2:
            character.isInAir = False
            velocityY = 0
        if keyboard.is_pressed("A"):
            character.posX -= 5 #PLAYER.SPEED
        if keyboard.is_pressed("D"):
            character.posX += 5 #PLAYER>SPEED
        if keyboard.is_pressed(" ") and character.isInAir == False:
            velocityY -= 15 #PLAYER.JUMPHEIGHT
            character.isInAir = True
        velocityY += 1 #GRAVITY
 
        if character.isInAir == True:
            character.posY += velocityY
        # Update the character's position
        draw()
 
        clock.tick(60)
