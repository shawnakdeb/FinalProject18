import pygame
import time
from block import Grid
from player import *
pygame.init()
gameDisplay = pygame.display.set_mode(((width+1)*grass.get_size()[0], (length+1)*grass.get_size()[1]))
Player1 = Player()
#Player2 = Player()
running = True
last_presssed = "down"
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        """if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:"""
                                           
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
            Player1.turn("up")
            if not (last_presssed == "up"):
                t0 = time.perf_counter()
            last_presssed = "up"
            if (keys[pygame.K_UP] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("up")
        elif keys[pygame.K_DOWN]:
            Player1.turn("down")
            if not (last_presssed == "down"):
                t0 = time.perf_counter()
            last_presssed = "down"
            if (keys[pygame.K_DOWN] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("down")
        elif keys[pygame.K_LEFT]:
            Player1.turn("left")
            if not (last_presssed == "left"):
                t0 = time.perf_counter()
            last_presssed = "left"
            if (keys[pygame.K_LEFT] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("left")
        elif keys[pygame.K_RIGHT]:
            Player1.turn("right")
            if not (last_presssed == "right"):
                t0 = time.perf_counter()
            last_presssed = "right"
            print(time.perf_counter()-t0)
            if (keys[pygame.K_RIGHT] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("right")
    pygame.display.flip()