import pygame, random
from pygame import *
import Pokemon, Move
from Battle import * 
#from Main import xsize, ysize
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman',50)
tinyfont = pygame.font.SysFont('Times New Roman',35)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
screen_size = (900,700)
text_blit_pos = (50,520)
active_player_pokemon = ""
active_opp_pokemon = ""

#gameDisplay = pygame.display.set_mode((xsize, ysize))
gameDisplay = pygame.display.set_mode(screen_size)
pygame.mixer.music.load('Battle Music.mp3')
pygame.mixer.music.play(-1)

battleback = pygame.image.load("battle back.jpg").convert()
battleback = pygame.transform.scale(battleback, screen_size)
opponent = pygame.image.load("opponent battle.png")
opponent = pygame.transform.scale2x(opponent)
player = pygame.image.load("redsprite.jpg").convert()
player.set_colorkey(WHITE)
player = pygame.transform.scale(player, (150, 200))

running = True

def flip():
        pygame.display.flip()

def update_top():
        pygame.display.update((0,0,900,250))

def update_bottom():
        pygame.display.update((0,300,900,200))

def update_text():
        pygame.display.update((0,500,900,300))

def blank_top():
        gameDisplay.blit(battleback,(0,0),(0,0, 900, 250))
        pygame.display.update((0,0,900,250))

def blank_bottom():
        gameDisplay.blit(battleback,(0,300),(0,300, 900, 200))
        pygame.display.update((0,300,900,200))

def blank_text():
        draw_rect()
        pygame.display.update((0,500,900,300))

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
    #flash()
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
    blit(text,text_blit_pos)
    flip()
    #wait(2000)
    blank()    

def blank():
    blit(battleback,(0,0))
    draw_rect()
    flip()

def send_opponent_pokemon(pok):
        global active_opp_pokemon
        active_opp_pokemon = pok
        blank_top()
        blank_text()
        prompt_text = myfont.render("Your opponent sent out "+pok.species+"!", True,BLACK)
        name_text = tinyfont.render(pok.species, True, BLACK) 
        lvl_text = tinyfont.render("LVL: "+str(pok.lvl), True, BLACK)
        hp_text = tinyfont.render("HP: "+str(pok.hp)+"/"+str(pok.max_hp), True, BLACK)
        opp_sprite = pok.sprite

        blit(prompt_text,text_blit_pos)
        blit(opp_sprite, (600, 90))
        blit(lvl_text, (200,115))
        blit(hp_text, (200,150))
        blit(name_text, (200,80))
        
        update_top()
        update_text()
        #wait(2000)

def send_player_pokemon(pok):
        global active_player_pokemon
        active_player_pokemon = pok
        blank_bottom()
        blank_text()
        prompt_text = myfont.render("GO "+pok.species+"!", True,BLACK)
        name_text = tinyfont.render(pok.species, True, BLACK) 
        lvl_text = tinyfont.render("LVL: "+str(pok.lvl), True, BLACK)
        hp_text = tinyfont.render("HP: "+str(pok.hp)+"/"+str(pok.max_hp), True, BLACK)
        play_sprite = pok.sprite
        
        blit(prompt_text, text_blit_pos)
        blit(play_sprite, (125, 325))
        blit(lvl_text, (500,360))
        blit(hp_text, (500,390))
        blit(name_text, (500,330))
        
        update_text()
        update_bottom()
        #wait(2000)


def double_size(img):
        return pygame.transform.scale2x(img)

def size_player_pok(img):
        return pygame.transform.scale(img, (150,150))

def rem_background(pok):
        img = pok.sprite.convert()
        #trans_color = img.get_at((0,0))
        img.set_colorkey(WHITE)
        pok.sprite = img


def user_choose_action(pok):
        blank_text()
        choice_text = myfont.render("Battle (b)      Switch (s)",True,BLACK)
        blit(choice_text, text_blit_pos)
        update_text()

def choose_move(pok):
        blank_text()
        moves_text1 = myfont.render(pok.moves[0]+" (1)    "+pok.moves[1]+" (2)", True, BLACK)
        moves_text2 = myfont.render(pok.moves[2]+" (3)    "+pok.moves[3]+" (4)", True, BLACK)
        blit(moves_text1, text_blit_pos)
        blit(moves_text2, (text_blit_pos[0], text_blit_pos[1]+50) )
        update_text()

def new_turn(user_pok, comp_pok, user_move, comp_move):
        if user_pok.spd >= comp_pok.spd:
                comp_damage = calcDamage(user_pok, comp_pok, user_move)
                comp_pok.hp -= comp_damage
                blank_text()
                battle_text = myfont.render(user_pok.species+" used "+user_move+"!",True, BLACK)
                blit(battle_text, text_blit_pos)
                update_text()
                wait(1000)
                update_opponent(comp_pok)
                
                if comp_pok.hp > 0:
                        user_damage = calcDamage(comp_pok,user_pok, comp_move)
                        user_pok.hp -= user_damage
                        blank_text()
                        battle_text = myfont.render("The opposing "+comp_pok.species+" used "+comp_move+"!",True, BLACK)
                        blit(battle_text, text_blit_pos)
                        update_text()
                        wait(1000)
                        update_player(user_pok)
                else:
                        return

        elif user_pok.spd < comp_pok.spd: 
                user_damage = calcDamage(comp_pok,user_pok, comp_move)
                user_pok.hp -= user_damage
                if user_pok.hp > 0:
                        comp_damage = calcDamage(user_pok,comp_pok, comp_move)
                        comp_pok.hp -= comp_damage
                else:
                        return

def update_opponent(pok):
        blank_top()
        name_text = tinyfont.render(pok.species, True, BLACK) 
        lvl_text = tinyfont.render("LVL: "+str(pok.lvl), True, BLACK)
        hp_text = tinyfont.render("HP: "+str(pok.hp)+"/"+str(pok.max_hp), True, BLACK)
        opp_sprite = pok.sprite

        blit(opp_sprite, (600, 90))
        blit(lvl_text, (200,115))
        blit(hp_text, (200,150))
        blit(name_text, (200,80))
        
        update_top()


def update_player(pok):
        blank_bottom()
        name_text = tinyfont.render(pok.species, True, BLACK) 
        lvl_text = tinyfont.render("LVL: "+str(pok.lvl), True, BLACK)
        hp_text = tinyfont.render("HP: "+str(pok.hp)+"/"+str(pok.max_hp), True, BLACK)
        play_sprite = pok.sprite
        
        blit(play_sprite, (125, 325))
        blit(lvl_text, (500,360))
        blit(hp_text, (500,390))
        blit(name_text, (500,330))
        
        update_bottom()


pika = Pokemon.Pokemon("Pikachu", 35, 55, 40, 90, 112, "pikachu forward2.jpg", 100, "Electric", ["Thunderbolt", "Rock Climb", "Surf", "Bug Buzz"] )
arbok = Pokemon.Pokemon("Arbok", 60, 95, 69, 80, 157, "arbok front.png", 60, "Poison", ["Sludge Bomb", "Brick Break", "Earthquake", "Rock Slide"] )
rem_background(arbok)
rem_background(pika)
pika.sprite = size_player_pok(pika.sprite)
arbok.sprite = double_size(arbok.sprite)
Pokemon.initialize(pika)
Pokemon.initialize(arbok)

opp_party = [arbok]
player_party = [pika]

initialize_battle()
send_opponent_pokemon(opp_party[0])
send_player_pokemon(player_party[0])

big_battle = True
choosing_action = True
choosing_move = False
switching = False
action = "nothing"

while big_battle:
        user_choose_action(active_player_pokemon)
        while choosing_action:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                choosing_action = False
                                big_battle = False
                
                        key = pygame.key.get_pressed()
                        
                        if key[pygame.K_s]:
                                action = "switch"
                        if key[pygame.K_b]:
                                action = "battle"
                        
                        if action == "battle":
                                choose_move(active_player_pokemon)
                                choosing_action = False
                                choosing_move = True
                                print(action)
                        elif action == "switch": 
                                #switch()
                                #switching = True
                                print(action)        
                        #action = "nada"

        choose_move(active_player_pokemon)
        while choosing_move:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                choosing_move = False
                                big_battle = False

                        key = pygame.key.get_pressed()
                        
                        if key[pygame.K_1]:
                                user_move = active_player_pokemon.moves[0]
                                choosing_move = False
                                break
                        elif key[pygame.K_2]:
                                user_move = active_player_pokemon.moves[1]
                                choosing_move = False
                                break
                        elif key[pygame.K_3]:
                                user_move = active_player_pokemon.moves[2]
                                choosing_move = False
                                break
                        elif key[pygame.K_4]:
                                user_move = active_player_pokemon.moves[3]
                                choosing_move = False
                                break
        comp_move = random.choice(active_opp_pokemon.moves)
        new_turn(active_player_pokemon, active_opp_pokemon, user_move, comp_move)
        break
                
                        