import dragon
import random

class Fire_Dragon(dragon.Dragon):
  '''
  Attributes
    1. Name and max_hp from super class
    2. f_shots - the number of fire shots the dragon has left
  '''
  #Initializes name, max_hp, and f_shots
  def __init__(self, name, max_hp, f_shots):
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  #overwritten method for a fire attack that deals a random value between 5-9 damage if the dragon has f_shots left
  def special_attack(self, other):
    if self.f_shots > 0:
      dmg = random.randint(5,9)
      other.take_damage(dmg)
      self.f_shots -= 1
      return f'{self._name} shoots a fireball at you and you take {dmg} damage!'
    else:
      return f'{self._name} tried to shoot a fireball at you but it didn\'t have any left! You take 0 damage.'

  #method to return the name of the dragon, its hp, and the number of fireballs left in a string
  def __str__(self):
    return super().__str__() + '\nFire shots remaining: ' + str(self.f_shots)
    
  