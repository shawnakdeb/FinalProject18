class Pokemon:

   def __init__(self,species,lvl,exp,types,moves,atk,defe,spd,hp,sprite, baseExp):
       self.species = species
       self.lvl = lvl
       self.exp = exp
       self.moves = moves
       self.atk = atk
       self.defe = defe
       self.spd = spd
       self.hp = hp
       self.sprite = sprite
       self.baseExp = baseExp

   def checkLvlUp(self):
       while self.exp > 4 / 5 * self.lvl * self.lvl * self.lvl:
           self.lvl+=1 
  
   def expGain(self, opp):
       self.exp += 2.1 * opp.baseExp * opp.lvl / 7

 

      


