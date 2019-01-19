import math
import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((700, 700))
from block import Grid
WHITE = (255,255,255)
grass = pygame.image.load('HGSS_Grass2.png').convert()
plain = pygame.image.load('plain.png').convert()
fieldlist = []
length = 12
width = 15
for x in range(width+1):
    fieldlist.append({})
    for y in range(length+1):
        if ((not ((x == 0 or x == width - 1) and y == length - 2)) and (x%2 == 0 and (y == 0 or y == length - 2))):
            fieldlist[x][y] = ((pygame.image.load('Tree1.png').convert()), True)
        elif ((not ((x == 1 or x == width) and y == length - 2)) and (x%2 == 1 and (y == 0 or y == length - 2))):
            fieldlist[x][y] = ((pygame.image.load('Tree2.png').convert()), True)
        elif ((not ((x == 0 or x == width - 1) and y == 2)) and (x%2 == 0 and (y == 2 or y == length))):
            fieldlist[x][y] = ((pygame.image.load('Tree5.png').convert()), False)
        elif ((not ((x == 1 or x == width) and y == 2)) and (x%2 == 1 and (y == 2 or y == length))):
            fieldlist[x][y] = ((pygame.image.load('Tree6.png').convert()), False)
        elif (((x == 0 or x == width - 1) and y%2 == 1) or (x%2 == 0 and (y == 1 or y == length - 1))):
            fieldlist[x][y] = ((pygame.image.load('Tree3.png').convert()), False)
        elif (((x == 1 or x == width) and y%2 == 1) or (x%2 == 1 and (y == 1 or y == length - 1))):
            fieldlist[x][y] = ((pygame.image.load('Tree4.png').convert()), False)
        elif ((x == 0 or x == width - 1) and y%2 == 0):
            fieldlist[x][y] = ((pygame.image.load('Tree7.png').convert()), False)
        elif ((x == 1 or x == width) and y%2 == 0):
            fieldlist[x][y] = ((pygame.image.load('Tree8.png').convert()), False)
        elif (x == 2 or x == width - 2 or y == 3):
            fieldlist[x][y] = (plain, True)
        else:    
            fieldlist[x][y] = (grass, True)
field = Grid(fieldlist)
class Player:
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
    sprites_left = [l1,ls,l2,ls]
    sprites_right = [r1,rs,r2,rs]
    sprites_forward = [f1,fs,f2,fs]
    sprites_back = [b1,bs,b2,bs]
    sprites = [sprites_left, sprites_right, sprites_forward, sprites_back]
    for l in sprites:
        for i in range (len(l)):
            l[i].set_colorkey(WHITE)
    def __init__(self, x, y ):
        self.sprite = self.fs
        self.x = x + .1736
        self.y = y + .5
        field.map_blit()
        gameDisplay.blit(self.sprite, (grass.get_size()[0]*self.x,grass.get_size()[1]*self.y))
    def blit(self):
        gameDisplay.blit(self.sprite, (grass.get_size()[0]*self.x,grass.get_size()[1]*self.y))
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
        field.blit(self.x, self.y)
        self.sprite = sprite_list[1]
        from Main import Player_list
        Player_list.sort(key=lambda p: p.y)
        for p in Player_list:
            p.blit()
        field.top_blit(self.x, self.y)
        pygame.display.flip()
    def walk (self, direction):
        sprite_list = []
        changex = 0
        changey = 0
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
        if (not (field.can_walk(math.floor(self.x) + (8*changex), math.ceil(self.y) + (8*changey)))):
            changex = 0
            changey = 0            
        for x in range (2):
            for i in sprite_list:
                field.blit(self.x, self.y)
                self.x += changex
                self.y += changey
                self.sprite = i
                from Main import Player_list
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    p.blit()
                field.top_blit(self.x, self.y)
                pygame.display.flip()
                pygame.time.wait(90)
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
        if (not (field.can_walk(math.floor(self.x) + (4*changex), math.ceil(self.y) + (4*changey)))):
            changex = 0
            changey = 0            
        for x in range (1):
            for i in sprite_list:
                field.blit(self.x, self.y)
                self.x += changex
                self.y += changey
                self.sprite = i
                from Main import Player_list
                Player_list.sort(key=lambda p: p.y)
                for p in Player_list:
                    p.blit()
                field.top_blit(self.x, self.y)
                pygame.display.flip()
                pygame.time.wait(75)

running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False