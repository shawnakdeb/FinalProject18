
import pygame       # import pygame module
def grassblit():
    for k,v in (grass_pos):
        gameDisplay.blit(grass_pos[(k,v)], (k,v))
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 1000))    # create a surface called 'screen' and give it a size of 1000x1000
pygame.mixer.music.load('Battle Music.mp3')
pygame.mixer.music.play(-1)
fs = pygame.image.load('still_front.png').convert()#17x23
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
grass = pygame.image.load('HGSS_Grass2.png').convert()
running = True      # used to control while loop
recx = 0
recy = 0
WHITE = (255,255,255)
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
grass.set_colorkey(WHITE)
grass_pos =  {}
for x in range (10):
    print(x)
    for y in range (10):
        grass_pos[(x*grass.get_size()[0],y*grass.get_size()[1])] = grass
        gameDisplay.blit(grass, (x*grass.get_size()[0],y*grass.get_size()[1]))
recx = 10*grass.get_size()[0]
for x in range (10):
    for y in range (10):
        grass_pos[(recx+x*grass.get_size()[0],recy+y*grass.get_size()[1])] = grass
        gameDisplay.blit(grass, (recx+x*grass.get_size()[0],recy+y*grass.get_size()[1]))
recx += 10*grass.get_size()[0]
for x in range (10):
    for y in range (10):
        grass_pos[(recx+x*grass.get_size()[0],recy+y*grass.get_size()[1])] = grass
        gameDisplay.blit(grass, (recx+x*grass.get_size()[0],recy+y*grass.get_size()[1]))
sx = 100
sy = 100
gameDisplay.blit(bs, (0,0))
while running:
    for e in pygame.event.get():    # get each event in the event queue... 
        """keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            sy -= 1
            gameDisplay.blit(bs, (sx,sy))
        if keys[pygame.K_DOWN]:
            sy += 1
            gameDisplay.blit(bs, (sx,sy))"""
        if e.type == pygame.QUIT:   # ...and if that event is QUIT...
            running = False
        """if e.type == pygame.KEYDOWN:
            if e.key == ord ( "a" ):
                sx+=1
                sy+=1
                gameDisplay.blit(bs, (sx,sy))"""
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        for x in range (2):
            grassblit()
            sy -= 2
            gameDisplay.blit(b1, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sy -= 2
            gameDisplay.blit(bs, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sy -= 2
            gameDisplay.blit(b2, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sy -= 2
            gameDisplay.blit(bs, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
    if keys[pygame.K_DOWN]:
        for x in range (2):
            grassblit()
            sy += 2
            gameDisplay.blit(f1, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sy += 2
            gameDisplay.blit(fs, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sy += 2
            gameDisplay.blit(f2, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sy += 2
            gameDisplay.blit(fs, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
    if keys[pygame.K_LEFT]:
        for x in range (2):
            grassblit()
            sx -= 2
            gameDisplay.blit(l1, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sx -= 2
            gameDisplay.blit(ls, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sx -= 2
            gameDisplay.blit(l2, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sx -= 2
            gameDisplay.blit(ls, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
    if keys[pygame.K_RIGHT]:
        for x in range (2):
            grassblit()
            sx += 2
            gameDisplay.blit(r1, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sx += 2
            gameDisplay.blit(rs, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sx += 2
            gameDisplay.blit(r2, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
            grassblit()
            sx += 2
            gameDisplay.blit(rs, (sx,sy))
            pygame.display.flip()
            pygame.time.wait(100)
    pygame.display.flip()