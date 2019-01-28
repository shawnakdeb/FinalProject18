import Pokemon
from Move import move
import pygame, math, random

pygame.init()

moves = {
    'Hydro Pump': move('Hydro Pump', 'Water', 110, 80, 5),
    'Thunderbolt': move('Thunderbolt', 'Electric', 90, 100, 15),
    'Bug Buzz': move('Bug Buzz', 'Bug', 90, 100, 15),
    'Rock Climb': move('Rock Climb', 'Normal', 90, 85, 20),
    'Sludge Bomb': move('Thunderbolt', 'Electric', 90, 100, 10),
    'Brick Break': move('Brick Break', 'Fighting', 75, 100, 15),
    'Earthquake': move('Earthquake', 'Ground', 100, 100, 10),
    'Rock Slide': move('Rock Slide', 'Rock', 75, 90, 10),
    'Surf': move('Surf', 'Water', 90, 100, 15),
}

def turn(atkP, defP, is_user_turn):
#    is_user_turn = False
#    print(atkP.species,"is attacking",defP.species,",who has HP =",defP.hp
    damage = calcDamage(atkP, defP, move)
#    print("Damage to",defP.species,":",damage)
    defP.hp -= damage
#    print(defP.species,"HP now =",defP.hp, "\n\n")

def comp_move(atkP):
    move_name = random.choice(atkP.moves)
    print(move_name)
    return moves[move_name]

def user_move(atkP):
    move_name = input("What move do you use?")
    while ( not move_name in atkP.moves):
       print ("That is not a move you know")
       move_name = input("What move do you use?")
    return moves[move_name]

def battle(userP, compP):
   while userP.hp > 0 and compP.hp > 0:
        if userP.spd >= compP.spd:
           turn(userP, compP, True)
           if compP.hp <= 0:
               return userP
           turn(compP, userP, False)
        else:
           turn(compP, userP, False)
           if userP.hp <= 0:
               return compP
           turn(userP, compP, True)
        
        if userP.hp <= 0:
            return compP
        if compP.hp <= 0:
            return userP
  

def calcMultiplier(move, defPok):
    key = (move.m_type, defPok.p_type)
    
    multiplier = 1
    check = {
        ('Fire', 'Water') : 0.5,
        ('Fire', 'Rock') : 0.5,
        ('Fire', 'Grass') : 2,
        ('Fire', 'Bug') : 2,
        ('Fire', 'Ice') : 2,
        ('Fire', 'Dragon') : 2,
        ('Fire', 'Fire') : 2,

        ('Bug', 'Fire') : 0.5,
        ('Bug', 'Flying') : 0.5,
        ('Bug', 'Grass') : 2,
        ('Bug', 'Poison') : 2,
        ('Bug', 'Psychic') : 2,
        ('Bug', 'Rock') : 0.5,
        ('Bug', 'Fighting') : 0.5,

        ('Electric', 'Electric') : 0.5,
        ('Electric', 'Flying') : 2,
        ('Electric', 'Grass') : 0.5,
        ('Electric', 'Ground') : 0,
        ('Electric', 'Water') : 2,
        ('Electric', 'Dragon') : 0.5,

        ('Fighting', 'Flying') : 0.5,
        ('Fighting', 'Ghost') : 0,
        ('Fighting', 'Ice') : 2,
        ('Fighting', 'Normal') : 2,
        ('Fighting', 'Psychic') : 0.5,
        ('Fighting', 'Rock') : 2,
        ('Fighting', 'Poison') : 0.5,
        ('Fighting', 'Bug') : 0.5,

        ('Flying', 'Bug') : 2,
        ('Flying', 'Electric') : 0.5,
        ('Flying', 'Fighting') : 2,
        ('Flying', 'Grass') : 2,
        ('Flying', 'Rock') : 0.5,
        
        ('Normal', 'Ghost') : 0,
        ('Normal', 'Fighting') : 0.5,

        ('Water', 'Fire') : 2,
        ('Water', 'Water') : 0.5,
        ('Water', 'Grass') : 0.5,
        ('Water', 'Ground') : 2,
        ('Water', 'Rock') : 2,
        ('Water', 'Dragon') : 0.5,

        ('Grass', 'Fire') : 0.5,
        ('Grass', 'Water') : 2,
        ('Grass', 'Grass') : 0.5,
        ('Grass', 'Poison') : 0.5,
        ('Grass', 'Ground') : 2,
        ('Grass', 'Flying') : 0.5,
        ('Grass', 'Bug') : 0.5,
        ('Grass', 'Rock') : 2,
        ('Grass', 'Dragon') : 0.5,

        ('Ice', 'Water') : 0.5,
        ('Ice', 'Grass') : 2,
        ('Ice', 'Ice') : 0.5,
        ('Ice', 'Ground') : 2,
        ('Ice', 'Flying') : 2,
        ('Ice', 'Dragon') : 2,

        ('Poison', 'Grass') : 2,
        ('Poison', 'Poison') : 0.5,
        ('Poison', 'Ground') : 0.5,
        ('Poison', 'Bug') : 2,
        ('Poison', 'Rock') : 0.5,
        ('Poison', 'Ghost') : 0.5,

        ('Ground', 'Poison') : 2,
        ('Ground', 'Fire') : 2,
        ('Ground', 'Electric') : 2,
        ('Ground', 'Grass') : 0.5,
        ('Ground', 'Flying') : 0,
        ('Ground', 'Bug') : 0.5,
        ('Ground', 'Rock') : 2,

        ('Psychic', 'Fighting') : 2,
        ('Psychic', 'Poison') : 2,
        ('Psychic', 'Psychic') : 0.5,

        ('Rock', 'Fire') : 2,
        ('Rock', 'Ice') : 2,
        ('Rock', 'Fighting') : 2,
        ('Rock', 'Ground') : 2,
        ('Rock', 'Flying') : 2,
        ('Rock', 'Bug') : 2,

        ('Ghost', 'Psychic') : 0,
        ('Ghost', 'Normal') : 0,
        ('Ghost', 'Ghost') : 2,

        ('Dragon', 'Dragon') : 2,
    }
    if key in check:
        multiplier = check[key]

    return multiplier

def calcDamage(atkPok, defPok, move):
    move_c = moves[move]
    typeMult = calcMultiplier(move_c, defPok)

    #print("Type Mod:",typeMult)
    
    randMult = random.randint(217, 255) / 255.0
    
   # print("Rand Mod:",randMult)

    STABMult = 1
    if(move_c.m_type == atkPok.p_type):
        STABMult = 1.5
    #print("STAB Mod:",STABMult)

    critMult = 1
    crit_prob = atkPok.base_spd / 512.0
    if random.random() < crit_prob:
        critMult = 2 

   # print("Crit Mod:",critMult)

    accMult = 1
    if random.randint(1,100) > move_c.accuracy:
        accMult = 0
  #  print("Acc Mod:",accMult)

    mod = typeMult * randMult * STABMult * critMult * accMult
   # print("Dam Mod:",mod)
    damage = math.floor(mod * ( (2*atkPok.lvl/5 + 2) * move_c.power * atkPok.atk / defPok.defe / 50 + 2))
    return damage     


pika = Pokemon.Pokemon("Pikachu", 35, 55, 40, 90, 112, "pikachu forward.jpg", 100, "Electric", ["Thunderbolt", "Rock Climb", "Surf", "Bug Buzz"] )
arbok = Pokemon.Pokemon("Arbok", 60, 95, 69, 80, 157, "arbok front.png", 60, "Poison", ["Sludge Bomb", "Brick Break", "Earthquake", "Rock Slide"] )
Pokemon.initialize(pika)
Pokemon.initialize(arbok)
"""print(t.lvl, t.atk, t.defe, t.spd, t.hp)
print(v.lvl, v.atk, v.defe, v.spd, v.hp)
"""
aWins = 0
pWins = 0
"""for x in range(10):
    winner = battle(t, v)
    print(winner.species,"wins")
    if winner.species == "Pikachu":
        pWins+=1
        Pokemon.update_stats(t,v)
    else:
        aWins+=1
        Pokemon.update_stats(v,t)
    Pokemon.restore_hp(t)
    Pokemon.restore_hp(v)
    print(t.lvl, t.atk, t.defe, t.spd, t.hp)
    print(v.lvl, v.atk, v.defe, v.spd, v.hp)
print(pWins)"""
#battle(t, v)
"""
running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
"""