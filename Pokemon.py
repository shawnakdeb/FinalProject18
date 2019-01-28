import math, random, pygame
pygame.init()

class Pokemon:

    def __init__(self, species, base_hp, base_atk, base_defe, base_spd, base_exp, sprite, exp, p_type, moves):
        self.species = species
        self.base_hp = base_hp
        self.base_atk = base_atk
        self.base_defe = base_defe
        self.base_spd = base_spd
        self.base_exp = base_exp
        if (type(sprite) == type("")):
            self.sprite = pygame.image.load(sprite)
        else:
            self.sprite = sprite
        self.moves = moves
        self.exp = exp
        self.lvl = 0
        self.atk = 0
        self.defe = 0
        self.spd = 0
        self.hp = 0
        self.max_hp = 0
        self.p_type = p_type
        self.isFainted = False

def copy(Poke):
    return Pokemon(Poke.species, Poke.base_hp, Poke.base_atk, Poke.base_defe, Poke.base_spd, Poke.base_exp, Poke.sprite, Poke.exp, Poke.p_type, Poke.moves)

def set_sprite(self, img):
    self.sprite = img

def calcLevel(pok):
    while pok.exp > 4 / 5 * pok.lvl * pok.lvl * pok.lvl and pok.lvl < 100:
         pok.lvl+=1        

def expGain(atkPok, oppPok):
     atkPok.exp += 2.1 * oppPok.base_exp * oppPok.lvl / 7
     calcLevel(atkPok)

def calcStats(pok):
    pok.atk = math.floor( ((pok.base_atk+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.defe = math.floor( ((pok.base_defe+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.spd = math.floor( ((pok.base_spd+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.max_hp = math.floor( ((pok.base_hp+25)*2+25)*pok.lvl/100.0 ) + pok.lvl + 10

def initialize(pok):
    calcLevel(pok)    
    pok.atk = math.floor( ((pok.base_atk+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.defe = math.floor( ((pok.base_defe+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.spd = math.floor( ((pok.base_spd+25)*2+25)*pok.lvl/100.0 ) + 5
    pok.max_hp = math.floor( ((pok.base_hp+25)*2+25)*pok.lvl/100.0 ) + pok.lvl + 10
    pok.hp = pok.max_hp

def restore_hp(pok):
    pok.hp = pok.max_hp

def update_stats(pok, deafPok):
    expGain(pok,deafPok)
    hpLost = pok.max_hp - pok.hp
    calcStats(pok)
    pok.hp = pok.max_hp - hpLost

def new_arbok():
    from BattleMain import rem_background, double_size
    arbok = Pokemon("Arbok", 60, 95, 69, 80, 157, "arbok front.png", 60, "Poison", ["Sludge Bomb", "Brick Break", "Earthquake", "Rock Slide"])
    rem_background(arbok)
    arbok.sprite = double_size(arbok.sprite)
    initialize(arbok)
    return arbok

running = False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
