import pygame
import random
import time
import os
from block import *
from Player import *
pygame.init()
print(os.getcwd())
xsize = (width+1)*grass.get_size()[0]
ysize = (length+1)*grass.get_size()[1]
gameDisplay = pygame.display.set_mode((xsize, ysize))
pygame.mixer.music.load('Route Music.mp3')
pygame.mixer.music.play(-1)
Player1 = Player(3,2)
#Player2= Player(3,4)
#Player3= Player(4,3)
Player_list=[Player1]#, Player2, Player3]
p_list = Player_list.copy()
p_list.remove(Player1)
"""for x in range (10):
    Player_list.append(Player())"""
Player1.turn("up")#import in player class doesn't fully run first call
running = True
last_presssed = "down"
t0 = time.perf_counter()
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
            if (not (last_presssed == "up")):
                Player1.turn("up")
                t0 = time.perf_counter()
                last_presssed = "up"
            if (keys[pygame.K_UP] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("up")
        elif keys[pygame.K_DOWN]:
            if not (last_presssed == "down"):
                Player1.turn("down")
                t0 = time.perf_counter()
                last_presssed = "down"
            if (keys[pygame.K_DOWN] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("down")
        elif keys[pygame.K_LEFT]:
            if not (last_presssed == "left"):
                Player1.turn("left")
                t0 = time.perf_counter()
                last_presssed = "left"
            if (keys[pygame.K_LEFT] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("left")
        elif keys[pygame.K_RIGHT]: 
            if not (last_presssed == "right"):
                Player1.turn("right")
                t0 = time.perf_counter()
                last_presssed = "right"
            if (keys[pygame.K_RIGHT] and ((time.perf_counter() - t0) > 0.2)):
                Player1.walk("right")
    if (random.random()<0.01):
        dir_list = ["up", "down", "right", "left"]
        ranchoices = random.choices(dir_list, k=len(p_list))
        for x in range(len(p_list)):
            p_list[x].walk(ranchoices[x])
    pygame.display.flip()