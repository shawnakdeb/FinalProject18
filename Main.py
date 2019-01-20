import pygame, os
from block import Grid
from player import *
pygame.init()
print(os.getcwd())
gameDisplay = pygame.display.set_mode(((width+1)*grass.get_size()[0], (length+1)*grass.get_size()[1]))
Player1 = Player()
#Player2 = Player()
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        """if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                Player1.turn("up") """                           
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if keys[pygame.K_UP]:
            Player1.run("up")
        if keys[pygame.K_DOWN]:
            Player1.run("down")
        if keys[pygame.K_LEFT]:
            Player1.run("left")
        if keys[pygame.K_RIGHT]:
            Player1.run("right")
    else:
        if keys[pygame.K_UP]:
            Player1.walk("up")
        if keys[pygame.K_DOWN]:
            Player1.walk("down")
        if keys[pygame.K_LEFT]:
            Player1.walk("left")
        if keys[pygame.K_RIGHT]:
            Player1.walk("right")
    pygame.display.flip()