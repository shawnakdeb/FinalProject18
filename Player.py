import math, random
import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((700, 700))
from block import *
from BattleMain import *
from Pokemon import *

WHITE = (255,255,255)
class Player:
    def __init__(self, x, y, color, dark_color, pokemon_list):
        #imports sprite images
        self.fs = pygame.image.load('still_front.png').convert()
        self.f1 = pygame.image.load('Forward_1.png').convert()
        self.f2 = pygame.image.load('Forward_2.png').convert()
        self.bs = pygame.image.load('still_back.png').convert()
        self.b1 = pygame.image.load('Back_1.png').convert()
        self.b2 = pygame.image.load('Back_2.png').convert()
        self.ls = pygame.image.load('still_left.png').convert()
        self.l1 = pygame.image.load('Left_1.png').convert()
        self.l2 = pygame.image.load('Left_2.png').convert()
        self.rs = pygame.image.load('still_right.png').convert()
        self.r1 = pygame.image.load('Right_1.png').convert()
        self.r2 = pygame.image.load('Right_2.png').convert()
        self.sprite_list = [self.fs, self.f1, self.f2, self.bs, self.b1, self.b2, self.ls, self.l1, self.l2, self.rs, self.r1, self.r2]
        self.sprites_left = [self.l1,self.ls,self.l2,self.ls]
        self.sprites_right = [self.r1,self.rs,self.r2,self.rs]
        self.sprites_forward = [self.f1,self.fs,self.f2,self.fs]
        self.sprites_back = [self.b1,self.bs,self.b2,self.bs]
        self.sprites = [self.sprites_left, self.sprites_right, self.sprites_forward, self.sprites_back]
        RED = (240, 104, 72)
        DARKRED = (192,56,56)
        if (not color == RED):
            for sprite in self.sprite_list:
                sprite.set_colorkey(WHITE)
                spixel = pygame.PixelArray(sprite)
                spixel.replace(DARKRED, dark_color)
                spixel.replace(RED, color, distance = 0.178443349898)
                spixel.close()
        else:
            for sprite in self.sprite_list:
                sprite.set_colorkey(WHITE)
        self.sprite = self.fs
        self.pokemon_list = pokemon_list
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
            if (p.field == self.field):
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
                    if (p.field == self.field):
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
        from Main import p_list
        for p in p_list:
            if (p.field == self.field):
                p.see_player(self)
        #starts wild pokemon encounter if applicable
        if (in_range((int) (self.x - .1736), (int) (self.y + 0.5)) and self.field.blocks[(int) (self.x - .1736)][(int) (self.y + 0.5)].wild and random.random() < 0.051):
            complete_battle(self.pokemon_list,[new_arbok()], False)
            self.field.map_blit()
            Player_list.sort(key=lambda p: p.y)
            for p in Player_list:
                if (p.field == self.field):
                    p.blit()

    
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
                    if (p.field == self.field):
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
        from Main import p_list
        for p in p_list:
            if (p.field == self.field):
                p.see_player(self)
        if (self.field.blocks[(int) (self.x + .1736)][(int) (self.y + 0.5)].wild and random.random() < 0.51):
            complete_battle(self.pokemon_list,[new_arbok()], False)
            self.field.map_blit()
            Player_list.sort(key=lambda p: p.y)
            for p in Player_list:
                if (p.field == self.field):
                    p.blit()

class Computer_Player(Player):
    def __init__(self, x, y, field, color, dark_color, direction, pokemon_list):
        Player.__init__(self, x, y, color, dark_color, pokemon_list)
        self.waiting = True
        self.field = field
        self.direction = direction
        if (direction == "up"):
            self.sprite = (self.bs)
        elif (direction == "left"):
            self.sprite = (self.ls)
        elif (direction == "right"):
            self.sprite = (self.rs)

    def walk(self, direction):
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
            return False            
        
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
                    if (p.field == self.field):
                        p.blit()
                self.field.top_blit(self.x, self.y)
                pygame.display.flip()
                pygame.time.wait(90)
    def see_player(self, User):
        can_walk = True
        if (self.waiting):
            if (self.direction == "left" and (self.x - User.x) < 10 and (self.x - User.x) > 0 and self.y == User.y):
                while(can_walk):
                    if (self.walk(self.direction) == False):
                        can_walk = False
                        self.waiting = False
                    complete_battle(User.pokemon_list,self.pokemon_list, True)
                    self.field.map_blit()
                    from Main import Player_list
                    Player_list.sort(key=lambda p: p.y)
                    for p in Player_list:
                        if (p.field == self.field):
                            p.blit()

            elif (self.direction == "right" and (User.x - self.x) < 10 and (User.x - self.x) > 0 and self.y == User.y):
                while(can_walk):
                    if (self.walk(self.direction) == False):
                        can_walk = False
                        self.waiting = False
                complete_battle(User.pokemon_list,self.pokemon_list, True)
                self.field.map_blit()
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    if (p.field == self.field):
                        p.blit()
            elif (self.direction == "down" and (User.y - self.y) < 10 and (User.y - self.y) > 0 and self.x == User.x):
                while(can_walk):
                    if (self.walk(self.direction) == False):
                        can_walk = False
                        self.waiting = False
                complete_battle(User.pokemon_list,self.pokemon_list, True)
                self.field.map_blit()
                from Main import Player_list
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    if (p.field == self.field):
                        p.blit()
            elif (self.direction == "up" and (self.y - User.y) < 10 and (self.y - User.y) > 0 and self.x == User.x):
                while(can_walk):
                    if (self.walk(self.direction) == False):
                        can_walk = False
                        self.waiting = False
                complete_battle(User.pokemon_list,self.pokemon_list, True)
                self.field.map_blit()
                from Main import Player_list
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    if (p.field == self.field):
                        p.blit()

running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False