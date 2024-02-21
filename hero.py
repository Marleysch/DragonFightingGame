import entity
import random

#Class for a Hero object
class Hero(entity.Entity):
  '''
  Attributes
  1. Name and max_hp from super class
  '''
#method for a basic attack that chooses 2 random values between 1-6 and adds them for the total damage
  def basic_attack(self, other):
    dmg = random.randint(1,6) + random.randint(1,6)
    other.take_damage(dmg)
    return f'You swing your sword at {other.name} and deal {dmg} damage!'

  #method for a special attack that chooses 1 random value betwen 1-12 for the total damage
  def special_attack(self, other):
    dmg = random.randint(1,12)
    other.take_damage(dmg)
    return f'You shoot your bow at {other._name} and deal {dmg} damage!'
    