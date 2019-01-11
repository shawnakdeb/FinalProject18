import pygame
from Player import Player
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 1000))
Player1 = Player()
running = True
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