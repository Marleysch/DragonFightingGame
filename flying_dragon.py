import dragon
import random

class Flying_Dragon(dragon.Dragon):
  '''
  Attributes
    1. Name and max_hp from super class
    2. swoops - the number of swoop attacks the dragon has left
  '''
  #Initializes name, max_hp, and swoops
  def __init__(self, name, max_hp, swoops):
    super().__init__(name, max_hp)
    self.swoops = swoops

  #overwritten method for a swoop attack that deals a random value between 5-8 damage if the dragon has swoops left
  def special_attack(self, other):
    if self.swoops > 0:
      dmg = random.randint(5,8)
      other.take_damage(dmg)
      self.swoops -= 1
      return f'{self._name} swoops at you with his claws and you take {dmg} damage!'
    else:
      return f'{self._name} tried to swoop at you but it didn\'t have any swoop attacks left! You take 0 damage.'

  #method to return the name of the dragon, its hp, and the number of fireballs left in a string
  def __str__(self):
    return super().__str__() + '\nSwoop attacks remaining: ' + str(self.swoops)