import pygame
#from Battle import * 
#from Main import xsize, ysize

pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
size = (900,700)

#gameDisplay = pygame.display.set_mode((xsize, ysize))
gameDisplay = pygame.display.set_mode(size)
pygame.mixer.music.load('Battle Music.mp3')
#pygame.mixer.music.play(-1)

battleback = pygame.image.load("battle back.jpg")
battleback = pygame.transform.scale(battleback, size)
opponent = pygame.image.load("opponent battle.png")
opponent = pygame.transform.scale2x(opponent)
player = pygame.image.load("redsprite.jpg")
player.set_colorkey(WHITE)
player = pygame.transform.scale(player, (150, 200))

running = True

def blit(thing, pos):
    gameDisplay.blit(thing, pos)

def draw_rect():
    pygame.draw.rect(gameDisplay,WHITE,(0,500,900,200))
    pygame.draw.rect(gameDisplay,BLUE,(0,500,900,200),6)
    pygame.draw.rect(gameDisplay,GREEN,(2,502,896,196),2)

def flash():
    for x in range(50):
        gameDisplay.fill(WHITE)
        pygame.display.flip()
        pygame.time.wait(10)
        gameDisplay.fill(BLACK)
        pygame.display.flip()

def initialize_battle():
    flash()
    draw_rect()    
    enemy_pos = (900,50)
    player_pos = (0,290)
    blit(opponent, enemy_pos)
    blit(player,player_pos)
    for x in range(110):
        blit(battleback,(0,0))
        draw_rect()
        enemy_pos = (enemy_pos[0] - 2, enemy_pos[1])
        player_pos = (player_pos[0] + 1, player_pos[1] )
        blit(player, player_pos)
        blit(opponent, enemy_pos)
        pygame.display.flip()
    
    
initialize_battle()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

