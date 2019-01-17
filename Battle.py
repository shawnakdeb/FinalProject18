from Pokemon import Pokemon
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True

@staticmethod
def turn(atkP, defP):
    pass
@staticmethod
def battle(userP, compP):
    while userP.hp > 0 and compP.hp > 0:
        if userP.spd >= compP.spd:
            turn(userP, compP)
            if compP.hp <= 0:
                break
            turn(compP, userP)
        else:
            turn(compP, userP)
            if compP.hp <= 0:
                break
            turn(userP, compP)
    
while running:

    for e in pygame.event.get():    # get each event in the event queue... 
    if e.type == pygame.QUIT:   # ...and if that event is QUIT...
        running = False         # ......set running to False so the main loop ends
