import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 1000))
WHITE = (255,255,255)
class Player:
    #17x23
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
    fs.set_colorkey(WHITE)
    f1.set_colorkey(WHITE)
    f2.set_colorkey(WHITE)
    bs.set_colorkey(WHITE)
    b1.set_colorkey(WHITE)
    b2.set_colorkey(WHITE)
    ls.set_colorkey(WHITE)
    l1.set_colorkey(WHITE)
    l2.set_colorkey(WHITE)
    rs.set_colorkey(WHITE)
    r1.set_colorkey(WHITE)
    r2.set_colorkey(WHITE)
    sprites_left = {l1,ls,l2,ls}
    sprites_right = {r1,rs,r2,rs}
    sprites_forward = {f1,fs,f2,fs}
    sprites_back = {b1,bs,b2,bs}
    def __init__(self):
        fs = pygame.image.load('still_front.png').convert()
        self.sprite = fs
        self.x = 100
        self.y = 100
    def move (self, direction):
        sprite_list = {}
        changex = 0
        changey = 0
        if (direction == "left"):
            sprite_list = sprites_left
            changex = -2
        elif (direction == "right"):
            sprite_list = sprites_right
            changex = 2
        elif (direction == "down"):
            sprite_list = sprites_forward
            changey = 2
        else:
            sprite_list = sprites_back
            changey = -2
        for x in range (1):
            for i in sprite_list:
                grassblit()
                self.x += changex
                self.y += changey
                gameDisplay.blit(i, (self.x,self.y))
                pygame.display.flip()
                pygame.time.wait(100)