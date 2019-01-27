import pygame
import math
import random
pygame.init()
gameDisplay = pygame.display.set_mode((700, 700))
BLACK = (0,0,0)
grass = pygame.image.load('HGSS_Grass2.png').convert()
plain = pygame.image.load('plain.png').convert()
Tree1 = pygame.image.load('Tree1.png').convert()
Tree2 = pygame.image.load('Tree2.png').convert()
Tree3 = pygame.image.load('Tree3.png').convert()
Tree4 = pygame.image.load('Tree4.png').convert()
Tree5 = pygame.image.load('Tree5.png').convert()
Tree6 = pygame.image.load('Tree6.png').convert()
Tree7 = pygame.image.load('Tree7.png').convert()
Tree8 = pygame.image.load('Tree8.png').convert()
Tree1Part = pygame.image.load('Tree1Part.png').convert()
Tree1Part.set_colorkey(BLACK)
Tree2Part = pygame.image.load('Tree2Part.png').convert()
Tree2Part.set_colorkey(BLACK)
length = 12
width = 15
def in_range(x, y):
    if (x == -1 or x == width+1 or y == -1 or y == length+1):
        return False
    else:
        return True
class Block:
    def __init__(self,x,y,image):
        self.walkable_var = (image == grass or image == plain or image == Tree1 or image == Tree2)
        self.coordinate = (x,y)
        self.realcoordinates = (image.get_size()[0]*x,image.get_size()[1]*y)
        self.image = image
        self.wild = (image == grass)
    def blit(self):
        gameDisplay.blit(self.image, self.realcoordinates)

    def walkable(self):
        from Main import Player_list
        walkable2 = True
        for p in (Player_list):
            if ((int(math.floor(p.x)),int(math.ceil(p.y))) == self.coordinate):
                walkable2 = False
        return (self.walkable_var and walkable2)

class Grid:
    def __init__(self, block_list):
        self.blocks = [[]]
        for x in range (len(block_list)):
            self.blocks.append([])
            for y in range (len(block_list[x])):
                self.blocks[x].append(Block(x,y,block_list[x][y]))
    def map_blit(self):
        for l in self.blocks:
            for b in range(len(l)):
                l[b].blit()
    def blit(self, x, y):
        if (in_range(int(math.ceil(x)),int(math.ceil(y)))):
            self.blocks[int(math.ceil(x))][int(math.ceil(y))].blit()
        if (in_range(int(math.floor(x)),int(math.floor(y)))):
            self.blocks[int(math.floor(x))][int(math.floor(y))].blit()
        if (in_range(int(math.floor(x)),int(math.ceil(y)))):
            self.blocks[int(math.floor(x))][int(math.ceil(y))].blit()
        if (in_range(int(math.ceil(x)),int(math.floor(y)))):
            self.blocks[int(math.ceil(x))][int(math.floor(y))].blit()
        if (in_range(int(math.floor(x)),int(math.ceil(y))+1)):
            self.blocks[int(math.floor(x))][int(math.ceil(y))+1].blit()
        if (in_range(int(math.ceil(x)),int(math.ceil(y))+1)):
            self.blocks[int(math.ceil(x))][int(math.ceil(y))+1].blit()
    def top_blit(self, x, y):
        xcoord = [int(math.ceil(x)), int(math.floor(x))]
        ycoord = [int(math.ceil(y)), int(math.floor(y)), int(math.ceil(y))+1]
        for i in xcoord:
            for j in ycoord:
                if (in_range(i,j)):
                    if (self.blocks[i][j].image == Tree1):
                        gameDisplay.blit(Tree1Part, self.blocks[i][j].realcoordinates)
                    elif (self.blocks[i][j].image == Tree2):
                        gameDisplay.blit(Tree2Part, self.blocks[i][j].realcoordinates)
    def can_walk(self, x, y):
        if (not in_range(int(x),int(y))):
            return True
        return self.blocks[int(x)][int(y)].walkable()

def left_clearing(fieldlist):
    fieldlist[0][length/2] = plain
    fieldlist[1][length/2] = plain
    fieldlist[0][(length/2) + 1] = plain
    fieldlist[1][(length/2) + 1] = plain
    fieldlist[0][(length/2) - 1] = plain
    fieldlist[1][(length/2) - 1] = plain
    fieldlist[0][(length/2) + 2] = Tree1
    fieldlist[1][(length/2) + 2] = Tree2
    fieldlist[0][(length/2) - 2] = Tree5
    fieldlist[1][(length/2) - 2] = Tree6

def right_clearing(fieldlist):
    fieldlist[width][length/2] = plain
    fieldlist[width-1][length/2] = plain
    fieldlist[width][(length/2) + 1] = plain
    fieldlist[width-1][(length/2) + 1] = plain
    fieldlist[width][(length/2) - 1] = plain
    fieldlist[width-1][(length/2) - 1] = plain
    fieldlist[width][(length/2) + 2] = Tree2
    fieldlist[width-1][(length/2) + 2] = Tree1
    fieldlist[width][(length/2) - 2] = Tree6
    fieldlist[width-1][(length/2) - 2] = Tree5

def top_clearing(fieldlist):
    fieldlist[int((width+1)/2)][0] = plain
    fieldlist[int((width+1)/2)][1] = plain
    fieldlist[int((width+1)/2)][2] = plain
    fieldlist[int(((width+1)/2)+1)][0] = plain
    fieldlist[int(((width+1)/2)+1)][1] = plain
    fieldlist[int(((width+1)/2)+1)][2] = plain
    fieldlist[int((width-1)/2)][0] = plain
    fieldlist[int((width-1)/2)][1] = plain
    fieldlist[int((width-1)/2)][2] = plain
    fieldlist[int(((width-1)/2)-1)][0] = plain
    fieldlist[int(((width-1)/2)-1)][1] = plain
    fieldlist[int(((width-1)/2)-1)][2] = plain

def bottom_clearing(fieldlist):
    fieldlist[int((width+1)/2)][length] = plain
    fieldlist[int((width+1)/2)][length-1] = plain
    fieldlist[int((width+1)/2)][length-2] = plain
    fieldlist[int(((width+1)/2)+1)][length] = plain
    fieldlist[int(((width+1)/2)+1)][length-1] = plain
    fieldlist[int(((width+1)/2)+1)][length-2] = plain
    fieldlist[int((width-1)/2)][length] = plain
    fieldlist[int((width-1)/2)][length-1] = plain
    fieldlist[int((width-1)/2)][length-2] = plain
    fieldlist[int(((width-1)/2)-1)][length] = plain
    fieldlist[int(((width-1)/2)-1)][length-1] = plain
    fieldlist[int(((width-1)/2)-1)][length-2] = plain

fieldlist = []

for x in range(width + 1):
    fieldlist.append({})
    for y in range(length + 1):
        if ((not ((x == 0 or x == width - 1) and y == length - 2)) and (x%2 == 0 and (y == 0 or y == length - 2))):
            fieldlist[x][y] = Tree1
        elif ((not ((x == 1 or x == width) and y == length - 2)) and (x%2 == 1 and (y == 0 or y == length - 2))):
            fieldlist[x][y] = Tree2
        elif ((not ((x == 0 or x == width - 1) and y == 2)) and (x%2 == 0 and (y == 2 or y == length))):
            fieldlist[x][y] = Tree5
        elif ((not ((x == 1 or x == width) and y == 2)) and (x%2 == 1 and (y == 2 or y == length))):
            fieldlist[x][y] = Tree6
        elif (((x == 0 or x == width - 1) and y%2 == 1) or (x%2 == 0 and (y == 1 or y == length - 1))):
            fieldlist[x][y] = Tree3
        elif (((x == 1 or x == width) and y%2 == 1) or (x%2 == 1 and (y == 1 or y == length - 1))):
            fieldlist[x][y] = Tree4
        elif ((x == 0 or x == width - 1) and y%2 == 0):
            fieldlist[x][y] = Tree7
        elif ((x == 1 or x == width) and y%2 == 0):
            fieldlist[x][y] = Tree8
        elif (x == 2 or x == width - 2 or y == 3):
            fieldlist[x][y] = plain
        else:
            fieldlist[x][y] = grass
left_clearing(fieldlist)
right_clearing(fieldlist)
top_clearing(fieldlist)
bottom_clearing(fieldlist)

field = Grid(fieldlist)

running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False