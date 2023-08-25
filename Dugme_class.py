
import pygame as pg
import random
import math
pg.init()
class Button:
  def __init__(self, centerx, centery, W, H, color, text, lightcolor, textcolor):
    self.centerx = centerx
    self.centery = centery
    self.W = W
    self.H = H
    self.color = color
    self.text = text
    self.lightcolor = lightcolor
    self.textcolor = textcolor

dugme1 = Button(300, 200, 250, 100, "red", "dugme", "pink", "aquamarine")


clock = pg.time.Clock
running = True
WIDTH = 640
HEIGHT = 480
screen = pg.display.set_mode((WIDTH , HEIGHT))

def drawdugme(dugme, highlight):
        if not highlight:
            pg.draw.rect(screen, dugme.color, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H/2, dugme.W, dugme.H))
            font1 = pg.font.SysFont('Comic Sans MS', math.floor(dugme.H*0.8))
            img1 = font1.render(dugme.text, True, dugme.textcolor)
            screen.blit(img1, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H*0.7))
        else:
            pg.draw.rect(screen, dugme.lightcolor, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H/2, dugme.W, dugme.H))
            font1 = pg.font.SysFont('Comic Sans MS', math.floor(dugme.H*0.8))
            img1 = font1.render(dugme.text, True, dugme.textcolor)
            screen.blit(img1, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H*0.7))
        pg.display.update()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    highlight = False
    if pg.mouse.get_pos()[0]> dugme1.centerx-dugme1.W/2 and pg.mouse.get_pos()[0]< dugme1.centerx+dugme1.W/2 and pg.mouse.get_pos()[1]> dugme1.centery-dugme1.H/2 and pg.mouse.get_pos()[1]< dugme1.centery+dugme1.H/2:
        highlight = True
    drawdugme(dugme1, highlight)
    
