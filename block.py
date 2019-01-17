import pygame
import math
import random

pygame.init()
gameDisplay = pygame.display.set_mode((700, 700))

class Block:
    def __init__(self,x,y,image,walkable):
        self.walkable = walkable
        self.coordinate = (x,y)
        self.realcoordinates = (image.get_size()[0]*x,image.get_size()[1]*y)
        self.image = image
    def blit(self):
        gameDisplay.blit(self.image, self.realcoordinates)

class Wild_Block:
    def __init__(self, x,y, image, wild_pokemon):
        Block.__init__(self, x, y, image)
    def wild_pokemon(self):
        if (random.random() < 0.051):
            #battle ensues
            pass

class Grid:
    def __init__(self, block_list):
        self.blocks = [[]]
        for x in range (len(block_list)):
            self.blocks.append([])
            for y in range (len(block_list[x])):
                self.blocks[x].append(Block(x,y,block_list[x][y][0],block_list[x][y][1]))
    def map_blit(self):
        for l in self.blocks:
            for b in range(len(l)):
                l[b].blit()
    def blit(self, x, y):
        self.blocks[int(math.ceil(x))][int(math.ceil(y))].blit()
        self.blocks[int(math.floor(x))][int(math.floor(y))].blit()
        self.blocks[int(math.floor(x))][int(math.ceil(y))].blit()
        self.blocks[int(math.ceil(x))][int(math.floor(y))].blit()
        self.blocks[int(math.floor(x))][int(math.ceil(y))+1].blit()
        self.blocks[int(math.ceil(x))][int(math.ceil(y))+1].blit()
    def top_blit(self, x, y):
        BLACK = (0,0,0)
        width = len(self.blocks) - 1
        length = len(self.blocks[0]) - 1
        xcoord = [int(math.ceil(x)), int(math.floor(x))]
        ycoord = [int(math.ceil(y)), int(math.floor(y)), int(math.ceil(y))+1]
        for i in xcoord:
            for j in ycoord:
                if ((not (i == 0 or i == width - 1)) and (i%2 == 0 and j == length - 2)):
                    Tree1Part = pygame.image.load('Tree1Part.png').convert()
                    Tree1Part.set_colorkey(BLACK)
                    gameDisplay.blit(Tree1Part, self.blocks[i][j].realcoordinates)
                elif ((not (i == 1 or i == width)) and (i%2 == 1 and j == length - 2)):
                    Tree2Part = pygame.image.load('Tree2Part.png').convert()
                    Tree2Part.set_colorkey(BLACK)
                    gameDisplay.blit(Tree2Part, self.blocks[i][j].realcoordinates)
    def can_walk(self, x, y):
        return self.blocks[int(x)][int(y)].walkable

running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False