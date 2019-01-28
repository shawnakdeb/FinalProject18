#driver file

import pygame
import random
import os
from block import *
from Player import *
from Pokemon import *
pygame.init()
import time

#sets up game display
xsize = (width+1)*grass.get_size()[0]
ysize = (length+1)*grass.get_size()[1]
gameDisplay = pygame.display.set_mode((xsize, ysize))

#plays background music
pygame.mixer.music.load('Route Music.mp3')
pygame.mixer.music.play(-1)

#colors for npc trainers
RED = (240, 104, 72)
DARKRED = (192,56,56)
BLUE = (168, 184, 208)
DARKBLUE = (64, 120, 192)
GREEN = (100, 229, 139)
DARKGREEN = (24, 178, 9)
YELLOW = (248, 197, 95)
DARKYELLOW = (225, 157, 0)
colors = [(BLUE,DARKBLUE), (GREEN,DARKGREEN), (YELLOW,DARKYELLOW)]
#Creates the pokemon
pika = Pokemon("Pikachu", 35, 55, 40, 90, 112, "pikachu forward2.jpg", 100, "Electric", ["Thunderbolt", "Rock Climb", "Surf", "Bug Buzz"])
arbok = new_arbok()
rem_background(pika)
pika.sprite = size_player_pok(pika.sprite)
initialize(pika)
arbok1 = new_arbok()
arbok2 = new_arbok()
arbok3 = new_arbok()

#creates players
Player1 = Player(3,2, RED, DARKRED, [pika])
Player2 = Computer_Player(7,4, field, BLUE, DARKBLUE, "up", [arbok1])
Player3 = Computer_Player(10,13, field2, GREEN, DARKGREEN, "left", [arbok2])
Player4 = Computer_Player(5,10, field, YELLOW, DARKYELLOW, "down", [arbok3])
Player_list=[Player1, Player2, Player3, Player4]
for x in range (20):
    color = random.choice(colors)
    Player_list.append(Computer_Player(random.randint(4,width-5), random.randint(4,length-5), random.choice(random.choice(field_array)), color[0], color[1], random.choice(["up", "down", "left", "right"]), [new_arbok()]))
p_list = Player_list.copy()
p_list.remove(Player1)
    
Player1.turn("up")
running = True

#variables to determine if the user tapped or held a button
last_presssed = "down"
t0 = time.perf_counter()

while running:
    """main loop"""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
                                           
    keys = pygame.key.get_pressed()

    #checks where the user wants to run to
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
        #checks where the user wants to walk (or just turn) to
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
    pygame.display.flip()