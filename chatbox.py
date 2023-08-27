import pygame as pg
import math
pg.init()

W = pg.display.Info().current_w - 400
H = pg.display.Info().current_h - 400
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
running = True

font = pg.font.Font(None, 32)
user_text = ''
user_text1 = 'A'
user_text2 = 'AA'
user_text3 = 'AAA'
user_text4 = 'AAAA'
user_text5 = 'AAAAA'
L = [user_text1, user_text2, user_text3, user_text4, user_text5]
w = 280
a = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and a:
            if event.key == pg.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pg.K_RETURN:
                user_text5 = user_text4
                user_text4 = user_text3
                user_text3 = user_text2
                user_text2 = user_text1
                user_text1 = user_text
                user_text = ''
                a = False
            else:
                user_text += event.unicode
    if (pg.mouse.get_pressed()[0] == True and pg.mouse.get_pos()[0] >= 15 and pg.mouse.get_pos()[0] <= 280 and pg.mouse.get_pos()[1] >= 155 and pg.mouse.get_pos()[1] <= 185):
        a = True
    screen.fill("White")
    pg.draw.rect(screen, "Black", (0, 0, 300, 190))
    pg.draw.rect(screen, "Gray", (10, 155, w, 30))
    text_surface = font.render(user_text, True, (0, 0, 0))
    text_surface1 = font.render(user_text1, True, (255, 255, 255))
    text_surface2 = font.render(user_text2, True, (255, 255, 255))
    text_surface3 = font.render(user_text3, True, (255, 255, 255))
    text_surface4 = font.render(user_text4, True, (255, 255, 255))
    text_surface5 = font.render(user_text5, True, (255, 255, 255))
    screen.blit(text_surface, (15, 160))
    screen.blit(text_surface1, (15, 130))
    screen.blit(text_surface2, (15, 100))
    screen.blit(text_surface3, (15, 70))
    screen.blit(text_surface4, (15, 40))
    screen.blit(text_surface5, (15, 10))
    w = max(280, text_surface.get_width() + 10)
    pg.display.flip()
    clock.tick(60)

pg.quit()
