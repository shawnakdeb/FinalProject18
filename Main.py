import pygame
from block import Grid
from player import Player
pygame.init()
gameDisplay = pygame.display.set_mode((700, 700))
grass = pygame.image.load('HGSS_Grass2.png').convert()
fieldlist = [[],[],[],[],[]]
for l in fieldlist:
    for x in range(len(l)):
        l[x] = grass
field = Grid((5,5), fieldlist)
Player1 = Player()
running = True
gameDisplay.blit(Player1.sprite, (Player1.x,Player1.y))
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Player1.move("up")
    if keys[pygame.K_DOWN]:
        Player1.move("down")
    if keys[pygame.K_LEFT]:
        Player1.move("left")
    if keys[pygame.K_RIGHT]:
        Player1.move("right")
    pygame.display.flip()