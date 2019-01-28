import pygame, random
from pygame import *
import Pokemon, Move
from Pokemon import update_stats, restore_hp, initialize
from Battle import calcDamage

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman',50) # creates text font
tinyfont = pygame.font.SysFont('Times New Roman',35) # creates font for printing level, name, hp
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
screen_size = (900,700)
text_blit_pos = (50,520)
active_player_pokemon = "" # initialize global user pokemon variable
active_opp_pokemon = "" # initialize global comp pokemon variable

gameDisplay = pygame.display.set_mode(screen_size)
pygame.mixer.music.load('Battle Music.mp3') # Loads battle music 
# pygame.mixer.music.play(-1)  

battleback = pygame.image.load("battle back.jpg").convert() # create user trainer sprite
battleback = pygame.transform.scale(battleback, screen_size)
opponent = pygame.image.load("opponent battle.png")     # create opponent trainer sprite
opponent = pygame.transform.scale2x(opponent)
player = pygame.image.load("redsprite.jpg").convert()
player.set_colorkey(WHITE) # removes white background
player = pygame.transform.scale(player, (150, 200))

running = True

def flip():
        """"Updates display"""
        pygame.display.flip()

def update_top():
        """"Updates top part of display that prints opponent's pokemon"""
        pygame.display.update((0,0,900,250))

def update_bottom():
        """"Updates bottom part of display that prints user's pokemon"""
        pygame.display.update((0,300,900,200))

def update_text():
        """Updates text part of display that prints display text"""
        pygame.display.update((0,500,900,300))

def blank_top():
        """"Clears top part of display that prints opponent's pokemon"""
        gameDisplay.blit(battleback,(0,0),(0,0, 900, 250))
        pygame.display.update((0,0,900,250))

def blank_bottom():
        """"Clears bottom part of display that prints user's pokemon"""
        gameDisplay.blit(battleback,(0,300),(0,300, 900, 200))
        pygame.display.update((0,300,900,200))

def blank_text():
        """Clears text part of display that prints display text"""
        draw_rect()
        pygame.display.update((0,500,900,300))

def blit(thing, pos):
        """Easy blit function"""
        gameDisplay.blit(thing, pos)

def draw_rect():
    """Draws text rectangle"""
    pygame.draw.rect(gameDisplay,WHITE,(0,500,900,200))
    pygame.draw.rect(gameDisplay,BLUE,(0,500,900,200),6)
    pygame.draw.rect(gameDisplay,GREEN,(2,502,896,196),2)

def flash():
    """Flashes screen to start battle (unused)"""
    for x in range(3):
        gameDisplay.fill(WHITE)
        flip()
        wait(100)
        gameDisplay.fill(BLACK)
        flip()
        wait(100)

def move_anim():
    """Flashes screen to signify damage taken (unused)"""
    for x in range(3):
        gameDisplay.fill(WHITE)
        flip()
        pygame.time.wait(100)
        gameDisplay.fill(RED)
        flip()
        pygame.time.wait(100)

def wait(time):
        """Easy wait function"""
        pygame.time.wait(time)

def initialize_battle(trainer):
        """Displays initial battle trainer animations and sends out first pokemon"""
        #flash()
        draw_rect()    # draws tect box
        enemy_pos = (900,50) 
        player_pos = (0,290)
        if (trainer):  # checks if battle is wild or trainer
                blit(opponent, enemy_pos)
        blit(player,player_pos)
        for x in range(110): # trainer move animation
                blit(battleback,(0,0))
                draw_rect()
                enemy_pos = (enemy_pos[0] - 2, enemy_pos[1])
                player_pos = (player_pos[0] + 1, player_pos[1] )
                blit(player, player_pos)
                if (trainer):
                        blit(opponent, enemy_pos)
                flip()
        if (trainer):
                text = myfont.render('You\'ve been challenged by an opponent!',True, BLACK)
        else:
                text = myfont.render('You\'ve been attacked by a wild pokemon!',True, BLACK)
        blit(text,text_blit_pos)
        flip()
        wait(2000)
        blank()    

def blank():
    """Clears screen"""
    blit(battleback,(0,0))
    draw_rect()
    flip()

def send_opponent_pokemon(pok):
        """Sends out computer pokemon at the start of battle"""
        global active_opp_pokemon
        active_opp_pokemon = pok # sets active computer pokemon to the input, pok
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
        wait(2000)

def send_player_pokemon(pok):
        """Sends out user pokemon at the start of battle"""
        global active_player_pokemon
        active_player_pokemon = pok     # sets active user pokemon to the input, pok
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
        wait(2000)


def double_size(img):
        """Doubles image size"""
        return pygame.transform.scale2x(img)

def size_player_pok(img):
        """Scales image size"""
        return pygame.transform.scale(img, (150,150))

def rem_background(pok):
        """Removes white background from sprites"""
        img = pok.sprite.convert()
        img.set_colorkey(WHITE)
        spixel = pygame.PixelArray(img) # addresses different shades of white
        spixel.replace(WHITE, (255,255,255), distance = 0.029)
        spixel.close()
        img.set_colorkey(WHITE)
        pok.sprite = img


def user_choose_action(pok):
        """Allows user to choose to battle"""
        blank_text()
        choice_text = myfont.render("Battle (b)",True,BLACK)
        blit(choice_text, text_blit_pos)
        update_text()

def choose_move(pok):
        """Allows user to choose their move using input"""
        blank_text()
        moves_text1 = myfont.render(pok.moves[0]+" (1)    "+pok.moves[1]+" (2)", True, BLACK)
        moves_text2 = myfont.render(pok.moves[2]+" (3)    "+pok.moves[3]+" (4)", True, BLACK)
        blit(moves_text1, text_blit_pos)
        blit(moves_text2, (text_blit_pos[0], text_blit_pos[1]+50) )
        update_text()

def new_turn(user_pok, comp_pok, user_move, comp_move):
        """Actual battling--hp deducted and status of battlers updated"""
        global choosing_action, choosing_move, big_battle, action
        action = "nothing" # default action
        choosing_action = True 
        choosing_move = False
        if user_pok.spd >= comp_pok.spd: # speed check to determine first to attack
                if user_pok.hp > 0: 
                        comp_damage = calcDamage(user_pok, comp_pok, user_move) # calculates damage using mechanics from method in Pokemon class
                        comp_pok.hp -= comp_damage
                        if comp_pok.hp < 0:
                                comp_pok.hp = 0 
                        blank_text()
                        battle_text = myfont.render(user_pok.species+" used "+user_move+"!",True, BLACK)
                        blit(battle_text, text_blit_pos)
                        update_text()
                        wait(1000)
                        update_opponent(comp_pok)
                else:
                        big_battle = False # ends battle
                        update_stats(comp_pok, user_pok) # gains exp points
                        return
                if comp_pok.hp > 0:     # makes sure first attack doesn't kill opponent
                        user_damage = calcDamage(comp_pok,user_pok, comp_move)
                        user_pok.hp -= user_damage
                        if user_pok.hp < 0:
                                user_pok.hp = 0
                        blank_text()
                        battle_text = myfont.render("The opposing "+comp_pok.species+" used "+comp_move+"!",True, BLACK)
                        blit(battle_text, text_blit_pos)
                        update_text()
                        wait(1000)
                        update_player(user_pok)
                else:
                        big_battle = False      # ends battle
                        update_stats(user_pok, comp_pok) # gains exp points
                        return

        elif user_pok.spd < comp_pok.spd: # speed check to determine first to attack
                if comp_pok.hp > 0:
                        user_damage = calcDamage(comp_pok, user_pok, comp_move)
                        user_pok.hp -= user_damage
                        if user_pok.hp < 0:
                                user_pok.hp = 0 
                        blank_text()
                        battle_text = myfont.render("The opposing "+comp_pok.species+" used "+comp_move+"!",True, BLACK)
                        blit(battle_text, text_blit_pos)
                        update_text()
                        wait(1000)
                        update_player(user_pok)
                else:
                        big_battle = False
                        update_stats(user_pok, comp_pok)
                        return
                if user_pok.hp > 0:
                        comp_damage = calcDamage(user_pok,comp_pok, user_move)
                        comp_pok.hp -= comp_damage
                        if comp_pok.hp < 0:
                                comp_pok.hp = 0
                        blank_text()
                        battle_text = myfont.render(user_pok.species+" used "+user_move+"!",True, BLACK)
                        blit(battle_text, text_blit_pos)
                        update_text()
                        wait(1000)
                        update_opponent(comp_pok)
                else:
                        big_battle = False
                        update_stats(comp_pok, user_pok)
                        return
                """user_damage = calcDamage(comp_pok,user_pok, comp_move)
                user_pok.hp -= user_damage
                if user_pok.hp > 0:
                        comp_damage = calcDamage(user_pok,comp_pok, comp_move)
                        comp_pok.hp -= comp_damage
                else:
                        return"""

def update_opponent(pok):
        """Redisplays opponent pokemon status"""
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
        """Redisplays player pokemon status"""
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

def restore_all():
        """Testing function that restarts battle after it finishes (unused)"""
        global big_battle, choosing_action, choosing_move, action
        restore_hp(active_player_pokemon)
        restore_hp(active_opp_pokemon)
        #initialize_battle()
        send_opponent_pokemon(opp_party[0])
        send_player_pokemon(player_party[0])
        big_battle = True
        choosing_action = True
        choosing_move = False
        action = "nothing"



def complete_battle(player_party, opp_party, trainer):
        """Function that runs entire battle. Takes in two parties of Pokemon, runs battle to completion and takes keyboard input"""
        global big_battle, choosing_action, choosing_move, action
        big_battle = True # battle running
        initialize_battle(trainer)
        send_opponent_pokemon(opp_party[0])
        send_player_pokemon(player_party[0])
        choosing_action = True
        choosing_move = False
        action = "nothing" # default action

        while big_battle:
                user_choose_action(active_player_pokemon)
                while choosing_action:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        choosing_action = False
                                        big_battle = False
                        
                                key = pygame.key.get_pressed()
                                
                                if key[pygame.K_b]:
                                        action = "battle"
                                
                                if action == "battle":
                                        choose_move(active_player_pokemon)
                                        choosing_action = False
                                        choosing_move = True
                                        #print(action)
                                
                        key = None

                choose_move(active_player_pokemon) # displays move possibilities
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
                comp_move = random.choice(active_opp_pokemon.moves)     # chooses random computer move from options 
                new_turn(active_player_pokemon, active_opp_pokemon, user_move, comp_move) # simulates one turn
                user_move = None
                comp_move = None
        if(active_player_pokemon.hp == 0):      # if player pokemon is defeated, reset to initial state at level 5
                active_player_pokemon.exp = 100
                initialize(active_player_pokemon)
        restore_hp(active_player_pokemon)       # at the end of battle, restore user pokemon's hp
        

# testing
""" 
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

#complete_battle(player_party, opp_party)


print(active_player_pokemon.species, ": new lvl -- ", active_player_pokemon.lvl)
print(active_opp_pokemon.species, ": new lvl -- ", active_opp_pokemon.lvl)                        """
