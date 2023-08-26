# TODO: Merge with main game

playerrect.x -= playervelocity.x * dt

    


    for y, row in enumerate(curroom):
        for x, tile in enumerate(row):
            if tile in [1,4] and playerrect.colliderect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32):
                if playervelocity.x < 0: 
                    playerrect.right = pygame.Rect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32).left
                elif playervelocity.x > 0: 
                    playerrect.left = pygame.Rect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32).right
            elif tile == 3 and playerrect.colliderect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32):
                if playerrect.x < window.get_width() / 2:
                    playerrect.x = window.get_width() - 80
                    roomcord.x -= 1
                    print(roomcord)
                elif playerrect.x > window.get_width() / 2:
                    playerrect.x = 60
                    roomcord.x += 1
                    print(roomcord)
                

    # worldoffset.y += playervelocity.y * dt
    playerrect.y -= playervelocity.y * dt
    for y, row in enumerate(curroom):
        for x, tile in enumerate(row):
            if tile in [1,4] and playerrect.colliderect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32):
                if playervelocity.y > 0: 
                    playerrect.top = pygame.Rect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32).bottom
                elif playervelocity.y < 0: 
                    playerrect.bottom = pygame.Rect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32).top
            elif tile == 3 and playerrect.colliderect(x * 32 + 60 - 64,y * 32 + 32 - 64,32,32):
                if playerrect.y < window.get_height() / 2:
                    playerrect.y = window.get_height() - 60
                    roomcord.y -= 1
                    print(roomcord)
                elif playerrect.y > window.get_height() / 2:
                    playerrect.y = 40
                    roomcord.y += 1
                    print(roomcord)

# citanje: matrica[y][x
# ]