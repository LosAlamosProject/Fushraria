import pygame as pg
import math
pg.init()

W = pg.display.Info().current_w
H = pg.display.Info().current_h - 400
screen = pg.display.set_mode((W, H))
screen.fill("Black")
clock = pg.time.Clock()
running = True

font1 = pg.font.SysFont('Comic Sans MS', 25, bold=pg.font.Font.bold)
a = 1
x = (W - 620) / 2
#DODAJTE SLIKE DOLE
image = pg.image.load("C:\\Users\\korisnik\\Downloads\\BlueCube.png").convert()
image1 = pg.image.load("C:\\Users\\korisnik\\Downloads\\RedCube.png").convert()
L = [image1, image, image1, 0, image1, image, 0, image, image1]
LB = [10, 5, 45, 0, 4, 63, 0, 9, 7]

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEWHEEL:
            if event.y > 0:
                a += 1
            if event.y < 0:
                a -= 1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                a = 1
            if event.key == pg.K_2:
                a = 2
            if event.key == pg.K_3:
                a = 3
            if event.key == pg.K_4:
                a = 4
            if event.key == pg.K_5:
                a = 5
            if event.key == pg.K_6:
                a = 6
            if event.key == pg.K_7:
                a = 7
            if event.key == pg.K_8:
                a = 8
            if event.key == pg.K_9:
               a = 9
    if a < 1:
        a = 9
    if a > 9:
        a = 1
    screen.fill("White")
    pg.draw.rect(screen, "Black", (x - 25,  H - 100, 670, 110))
    if (a == 1):
        pg.draw.rect(screen, "Gold", (x - 5,  H - 80, 70, 70))
    elif (a == 2):
        pg.draw.rect(screen, "Gold", (x + 70 - 5,  H - 80, 70, 70))
    elif (a == 3):
        pg.draw.rect(screen, "Gold", (x + 70 * 2 - 5,  H - 80, 70, 70))
    elif (a == 4):
        pg.draw.rect(screen, "Gold", (x + 70 * 3 - 5,  H - 80, 70, 70))
    elif (a == 5):
        pg.draw.rect(screen, "Gold", (x + 70 * 4 - 5,  H - 80, 70, 70))
    elif (a == 6):
        pg.draw.rect(screen, "Gold", (x + 70 * 5 - 5,  H - 80, 70, 70))
    elif (a == 7):
        pg.draw.rect(screen, "Gold", (x + 70 * 6 - 5,  H - 80, 70, 70))
    elif (a == 8):
        pg.draw.rect(screen, "Gold", (x + 70 * 7 - 5,  H - 80, 70, 70))
    elif (a == 9):
        pg.draw.rect(screen, "Gold", (x + 70 * 8 - 5,  H - 80, 70, 70))
    pg.draw.rect(screen, "Gray", (x,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 2,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 3,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 4,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 5,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 6,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 7,  H - 75, 60, 60))
    pg.draw.rect(screen, "Gray", (x + 70 * 8,  H - 75, 60, 60))
    if (L[0] != 0):
        screen.blit(L[0], (x + 5,  H - 70))
        img1 = font1.render(str(int(LB[0])), True, 'Black')
        if LB[0] < 10:
            screen.blit(img1, (x + 40,  H - 45))
        else:
            screen.blit(img1, (x + 30,  H - 45))
    if (L[1] != 0):
        screen.blit(L[1], (x + 75,  H - 70))
        img1 = font1.render(str(int(LB[1])), True, 'Black')
        if LB[1] < 10:
            screen.blit(img1, (x + 70 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 + 30,  H - 45))
    if (L[2] != 0):
        screen.blit(L[2], (x + 70 * 2 + 5,  H - 70))
        img1 = font1.render(str(int(LB[2])), True, 'Black')
        if LB[2] < 10:
            screen.blit(img1, (x + 70 * 2 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 2 + 30,  H - 45))
    if (L[3] != 0):
        screen.blit(L[3], (x + 70 * 3 + 5,  H - 70))
        img1 = font1.render(str(int(LB[3])), True, 'Black')
        if LB[3] < 10:
            screen.blit(img1, (x + 70 * 3 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 3 + 30,  H - 45))
    if (L[4] != 0):
        screen.blit(L[4], (x + 70 * 4 + 5,  H - 70))
        img1 = font1.render(str(int(LB[4])), True, 'Black')
        if LB[4] < 10:
            screen.blit(img1, (x + 70 * 4 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 4 + 30,  H - 45))
    if (L[5] != 0):
        screen.blit(L[5], (x + 70 * 5 + 5,  H - 70))
        img1 = font1.render(str(int(LB[5])), True, 'Black')
        if LB[5] < 10:
            screen.blit(img1, (x + 70 * 5 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 5 + 30,  H - 45))
    if (L[6] != 0):
        screen.blit(L[6], (x + 70 * 6 + 5,  H - 70))
        img1 = font1.render(str(int(LB[6])), True, 'Black')
        if LB[6] < 10:
            screen.blit(img1, (x + 70 * 6 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 6 + 30,  H - 45))
    if (L[7] != 0):
        screen.blit(L[7], (x + 70 * 7 + 5,  H - 70))
        img1 = font1.render(str(int(LB[7])), True, 'Black')
        if LB[7] < 10:
            screen.blit(img1, (x + 70 * 7 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 7 + 30,  H - 45))
    if (L[8] != 0):
        screen.blit(L[8], (x + 70 * 8 + 5,  H - 70))
        img1 = font1.render(str(int(LB[8])), True, 'Black')
        if LB[8] < 10:
            screen.blit(img1, (x + 70 * 8 + 40,  H - 45))
        else:
            screen.blit(img1, (x + 70 * 8 + 30,  H - 45))
    pg.display.update()
    clock.tick(60)

pg.quit()
