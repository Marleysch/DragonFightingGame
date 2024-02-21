import entity
import random

class Dragon(entity.Entity):
  '''
  Attributes
  1. Name and max_hp from super class
  '''
  #method for a basic attack that chooses random value between 3-7 for total damage
  def basic_attack(self, other):
    dmg = random.randint(3,7)
    other.take_damage(dmg)
    return(f'{self._name} swings his tail at the hero and deals {dmg} damage!')

  #method for a special attack that chooses 1 random value betwen 4-8 for the total damage
  def special_attack(self, other):
    dmg = random.randint(4,8)
    other.take_damage(dmg)
    return(f'{self._name} swipes at you with his claws and deals {dmg} damage!')