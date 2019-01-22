import math, random 

class Pokemon:

   def __init__(self, species, base_hp, base_atk, base_defe, base_spd, base_exp, sprite, exp, p_type, moves):
       self.species = species
       self.base_hp = base_hp
       self.base_atk = base_atk
       self.base_defe = base_defe
       self.base_spd = base_spd
       self.base_exp = base_exp
       self.sprite = sprite
       self.moves = moves
       self.exp = exp
       self.lvl = 0
       self.atk = 0
       self.defe = 0
       self.spd = 0
       self.hp = 0
       self.sprite = sprite
       self.p_type = p_type
       self.isFainted = False

def checkLvlUp(a):
    while a.exp > 4 / 5 * a.lvl * a.lvl * a.lvl and a.lvl < 100:
        a.lvl+=1 

def expGain(atkPok, oppPok):
    atkPok.exp += 2.1 * oppPok.base_exp * oppPok.lvl / 7

def calcStats(pok):
    pok.atk = math.floor( ((pok.base_atk+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.defe = math.floor( ((pok.base_defe+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.spd = math.floor( ((pok.base_spd+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.hp = math.floor( ((pok.base_hp+25)*2+25)*pok.lvl/100.0 ) + pok.lvl + 10
    