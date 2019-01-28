import math, random
import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((700, 700))
from block import *
#from Battle import *

WHITE = (255,255,255)
class Player:

    #imports sprite images
    fs = pygame.image.load('still_front.png').convert()
    f1 = pygame.image.load('Forward_1.png').convert()
    f2 = pygame.image.load('Forward_2.png').convert()
    bs = pygame.image.load('still_back.png').convert()
    b1 = pygame.image.load('Back_1.png').convert()
    b2 = pygame.image.load('Back_2.png').convert()
    ls = pygame.image.load('still_left.png').convert()
    l1 = pygame.image.load('Left_1.png').convert()
    l2 = pygame.image.load('Left_2.png').convert()
    rs = pygame.image.load('still_right.png').convert()
    r1 = pygame.image.load('Right_1.png').convert()
    r2 = pygame.image.load('Right_2.png').convert()
    sprite_list = [fs, f1, f2, bs, b1, b2, ls, l1, l2, rs, r1, r2]
    sprites_left = [l1,ls,l2,ls]
    sprites_right = [r1,rs,r2,rs]
    sprites_forward = [f1,fs,f2,fs]
    sprites_back = [b1,bs,b2,bs]
    sprites = [sprites_left, sprites_right, sprites_forward, sprites_back]
    
    for l in sprites:
        for i in range (len(l)):
            l[i].set_colorkey(WHITE)

    def __init__(self, x, y, color):
        RED = (240, 104, 72)
        BLUE = (77, 129, 214)
        GREEN = (24, 178, 9)
        YELLOW = (248, 197, 95)
        if (not color == RED):
            if ( color == BLUE):
                for sprite in self.sprite_list:
                    sprite.set_colorkey(WHITE)
                    spixel = pygame.PixelArray(sprite)
                    spixel.replace(RED, BLUE, distance = 0.178443349898)
                    spixel.close()
            if (color == GREEN):
                for sprite in self.sprite_list:
                    sprite.set_colorkey(WHITE)
                    spixel = pygame.PixelArray(sprite)
                    spixel.replace(RED, color, distance = 0.178443349898)
                    spixel.close()
            if (color == YELLOW):
                for sprite in self.sprite_list:
                    sprite.set_colorkey(WHITE)
                    spixel = pygame.PixelArray(sprite)
                    spixel.replace(RED, color, distance = 0.178443349898)
                    spixel.close()
        self.sprite = self.fs
        self.x = x + .1736
        self.y = y + .5
        self.i = 1
        self.j = 1
        self.field = field_array[self.j][self.i]
        self.field.map_blit()
        gameDisplay.blit(self.sprite, (grass.get_size()[0]*self.x,grass.get_size()[1]*self.y))
    
    #displays current sprite of player
    def blit(self):
        gameDisplay.blit(self.sprite, (grass.get_size()[0]*self.x,grass.get_size()[1]*self.y))
    
    #changes which grid the player is on
    def change_field(self):
        self.field = field_array[self.j][self.i]
        self.field.map_blit()
        self.blit()
    
    #the player turns in a given direction
    def turn(self, direction):
        sprite_list = []
        if (direction == "left"):
            sprite_list = self.sprites_left.copy()
        elif (direction == "right"):
            sprite_list = self.sprites_right.copy()
        elif (direction == "down"):
            sprite_list = self.sprites_forward.copy()
        else:
            sprite_list = self.sprites_back.copy()
        self.field.blit(self.x, self.y)
        self.sprite = sprite_list[1]
        from Main import Player_list
        Player_list.sort(key=lambda p: p.y)
        for p in Player_list:
            p.blit()
        self.field.top_blit(self.x, self.y)
        pygame.display.flip()
    
    #the player walks in a given direction
    def walk (self, direction):
        sprite_list = []
        changex = 0
        changey = 0
        #Determines direction
        if (direction == "left"):
            sprite_list = self.sprites_left.copy()
            changex = -0.125
        elif (direction == "right"):
            sprite_list = self.sprites_right.copy()
            changex = 0.125
        elif (direction == "down"):
            sprite_list = self.sprites_forward.copy()
            changey = 0.125
        else:
            sprite_list = self.sprites_back.copy()
            changey = -0.125
        #if the player can't walk on the tile, the player will walk in place
        if (not (self.field.can_walk(math.floor(self.x) + (8*changex), math.ceil(self.y) + (8*changey)))):
            changex = 0
            changey = 0            
        
        #walking motion (alternating through multiple sprites)
        for x in range (2):
            for i in sprite_list:
                self.field.blit(self.x, self.y)
                self.x += changex
                self.y += changey
                self.sprite = i
                from Main import Player_list
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    p.blit()
                self.field.top_blit(self.x, self.y)
                pygame.display.flip()
                pygame.time.wait(90)
            #checks if the player is leaving the current field
            if (((grass.get_size()[0]*self.x) + (self.sprite.get_size()[0]/2))/grass.get_size()[0] < 0.25):
                self.x += width + 1
                self.i -= 1
                self.change_field()
            elif (((grass.get_size()[0]*self.x) + (self.sprite.get_size()[0]/2))/grass.get_size()[0] > width+0.75):
                self.x -= width + 1
                self.i += 1
                self.change_field()
            elif (((grass.get_size()[1]*self.y) + (self.sprite.get_size()[1]/2))/grass.get_size()[1] < 0):
                self.y += length + 1
                self.j -= 1
                self.change_field()
            elif (((grass.get_size()[1]*self.y) + (self.sprite.get_size()[1]/2))/grass.get_size()[1] > length+0.5):
                self.y -= length + 1
                self.j += 1
                self.change_field()

        #starts wild pokemon encounter if applicable
        #if (in_range((int) (self.x - .1736), (int) (self.y + 0.5)) and self.field.blocks[(int) (self.x - .1736)][(int) (self.y + 0.5)].wild and random.random() < 0.051):
        #    battle(t,v)
    
    #the player runs (speed walks) in a given direction
    #same mechanics as walking, except with longer strides and shorter time between steps
    def run (self, direction):
        sprite_list = []
        changex = 0
        changey = 0
        if (direction == "left"):
            sprite_list = self.sprites_left.copy()
            changex = -0.25
        elif (direction == "right"):
            sprite_list = self.sprites_right.copy()
            changex = 0.25
        elif (direction == "down"):
            sprite_list = self.sprites_forward.copy()
            changey = 0.25
        else:
            sprite_list = self.sprites_back.copy()
            changey = -0.25
        if (not (self.field.can_walk(math.floor(self.x) + (4*changex), math.ceil(self.y) + (4*changey)))):
            changex = 0
            changey = 0            
        for x in range (1):
            for i in sprite_list:
                self.field.blit(self.x, self.y)
                self.x += changex
                self.y += changey
                self.sprite = i
                from Main import Player_list
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    p.blit()
                self.field.top_blit(self.x, self.y)
                pygame.display.flip()
                pygame.time.wait(75)
            if (((grass.get_size()[0]*self.x) + (self.sprite.get_size()[0]/2))/grass.get_size()[0] < 0.25):
                self.x += width + 1
                self.i -= 1
                self.change_field()
            elif (((grass.get_size()[0]*self.x) + (self.sprite.get_size()[0]/2))/grass.get_size()[0] > width+0.75):
                self.x -= width + 1
                self.i += 1
                self.change_field()
            elif (((grass.get_size()[1]*self.y) + (self.sprite.get_size()[1]/2))/grass.get_size()[1] < 0):
                self.y += length + 1
                self.j -= 1
                self.change_field()
            elif (((grass.get_size()[1]*self.y) + (self.sprite.get_size()[1]/2))/grass.get_size()[1] > length+0.5):
                self.y -= length + 1
                self.j += 1
                self.change_field()
        #if (self.field.blocks[(int) (self.x + .1736)][(int) (self.y + 0.5)].wild and random.random() < 0.51):
        #    battle(t,v)

running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False