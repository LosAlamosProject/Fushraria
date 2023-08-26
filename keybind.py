import pygame as pg
import random
import math
pg.init()
kb="k"
ps=0

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

dugme1 = Button(300, 200, 350, 100, "red", "dugme", "pink", "darkblue")

clock = pg.time.Clock
running = True
WIDTH = 960
HEIGHT = 480
screen = pg.display.set_mode((WIDTH , HEIGHT))

txt=''

def drawdugme(dugme, highlight,klik):
  global ps
  global txt
  kk=dugme.centerx-dugme.W/2
  if klik:
    ps=1
    txt = 'Keybind: "-"'
    dugme.text=txt
  if not highlight:
    pg.draw.circle(screen, dugme.color,(kk, dugme.centery-dugme.H/2+50),50)
    pg.draw.circle(screen, dugme.color,(kk+dugme.W, dugme.centery-dugme.H/2+50),50)
    pg.draw.rect(screen, dugme.color, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H/2, dugme.W, dugme.H))
    font1 = pg.font.SysFont('Arial', math.floor(dugme.H*0.8))
    img1 = font1.render(dugme.text, True, dugme.textcolor)
    screen.blit(img1, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H*0.5))
  else:
    pg.draw.circle(screen, dugme.lightcolor,(kk,dugme.centery-dugme.H/2+50),50)
    pg.draw.circle(screen, dugme.lightcolor,(kk+dugme.W, dugme.centery-dugme.H/2+50),50)
    pg.draw.circle(screen, dugme.lightcolor,(175,200),50)
    pg.draw.circle(screen, dugme.lightcolor,(425,200),50)
    pg.draw.rect(screen, dugme.lightcolor, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H/2, dugme.W, dugme.H))
    font1 = pg.font.SysFont('Arial', math.floor(dugme.H*0.8))
    img1 = font1.render(dugme.text, True, dugme.textcolor)
    screen.blit(img1, (dugme.centerx-dugme.W/2, dugme.centery-dugme.H*0.5))
  pg.display.update()

while running:
  screen.fill("white")
  highlight = False
  if pg.Rect(dugme1.centerx-dugme1.W/2, dugme1.centery-dugme1.H/2, dugme1.W, dugme1.H).collidepoint(pg.mouse.get_pos()):
      highlight = True
  klik = pg.mouse.get_pressed()[0]
  klik = klik and highlight
  drawdugme(dugme1, highlight, klik)
  for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
      if event.type == pg.KEYDOWN and ps>=1:
        try:
          dugme1.text = 'Keybind: '+str(chr(event.key))
          ps=0
        except: print(event.key)
