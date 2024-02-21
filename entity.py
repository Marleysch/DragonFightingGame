import abc

# Creates a class that will create either the hero or dragon class
class Entity:
  '''Attributes:
   _name – entity’s name, 
   _hp – entity’s hit points, 
   _max_hp – entity’s starting hp
   '''
  def __init__(self, name, max_hp):
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  def take_damage(self, dmg):
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0
    return self._hp

  def __str__(self):
    return  str(self._name) + " " + str(self._hp) + "/" + str(self._max_hp)

  # The abstract that other classes will overwrite
  @abc.abstractmethod
  def basic_attack(self, other):
    pass

  def special_attack(self, other):
    pass