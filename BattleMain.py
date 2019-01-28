import pygame
import Pokemon, Move
from Battle import * 
#from Main import xsize, ysize
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman',50)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
size = (900,700)

#gameDisplay = pygame.display.set_mode((xsize, ysize))
gameDisplay = pygame.display.set_mode(size)
pygame.mixer.music.load('Battle Music.mp3')
pygame.mixer.music.play(-1)

battleback = pygame.image.load("battle back.jpg")
battleback = pygame.transform.scale(battleback, size)
opponent = pygame.image.load("opponent battle.png")
opponent = pygame.transform.scale2x(opponent)
player = pygame.image.load("redsprite.jpg")
player.set_colorkey(WHITE)
player = pygame.transform.scale(player, (150, 200))

running = True

def flip():
        pygame.display.flip()
def blit(thing, pos):
    gameDisplay.blit(thing, pos)

def draw_rect():
    pygame.draw.rect(gameDisplay,WHITE,(0,500,900,200))
    pygame.draw.rect(gameDisplay,BLUE,(0,500,900,200),6)
    pygame.draw.rect(gameDisplay,GREEN,(2,502,896,196),2)

def flash():
    for x in range(3):
        gameDisplay.fill(WHITE)
        flip()
        wait(100)
        gameDisplay.fill(BLACK)
        flip()
        wait(100)

def move_anim():
    for x in range(3):
        gameDisplay.fill(WHITE)
        flip()
        pygame.time.wait(100)
        gameDisplay.fill(RED)
        flip()
        pygame.time.wait(100)

def wait(time):
        pygame.time.wait(time)

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
        flip()
    text = myfont.render('You\'ve been challenged by an opponent!',True, BLACK)
    blit(text,(50,520))
    flip()
    wait(2000)
        

def blank():
    blit(battleback,(0,0))
    draw_rect()
    flip()

def opponent_pokemon(pok):
        blank()
        text = myfont.render("Your opponent sent out "+pok.species+"!", True,BLACK)
        blit(text,(50,520))
        opp_sprite = pok.sprite
        blit(opp_sprite, (600, 100))
        flip()

def rem_background(pok):
        pok.sprite.convert()
        trans_color = pok.sprite.get_at((5,5))
        print(trans_color)
        pok.sprite.set_colorkey(trans_color)
        print(pok.sprite.get_colorkey)
        

pika = Pokemon.Pokemon("Pikachu", 35, 55, 40, 90, 112, "pikachu forward.jpg", 100, "Electric", ["Thunderbolt", "Rock Climb", "Surf", "Bug Buzz"] )
arbok = Pokemon.Pokemon("Arbok", 60, 95, 69, 80, 157, "arbok front.png", 60, "Poison", ["Sludge Bomb", "Brick Break", "Earthquake", "Rock Slide"] )
rem_background(arbok)
rem_background(pika)

opp_party = [arbok]
player_party = [pika]
initialize_battle()
opponent_pokemon(opp_party[0])
player_pokemon = (player_party[0])

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

