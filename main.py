
#Marley Schneider, Rene Trujillo
#10/11/23
#Program that uses classes to create a turn style game where user can fight dragons
import random
import hero
import dragon
import fire_dragon
import flying_dragon
import check_input

def main():

  # initialises an empty list and then inserts each dragon object into this list
  dragon_list = []
  dragon1 = dragon.Dragon('Deadly Nadder', 10)
  dragon_list.append(dragon1)
  fire_dragon1 = fire_dragon.Fire_Dragon('Gronckle', 15,3)
  dragon_list.append(fire_dragon1)
  flying_dragon1 = flying_dragon.Flying_Dragon('Timberjack', 20,5)
  dragon_list.append(flying_dragon1)

  # Asks the user to enter the name of the hero and the creates the hero object with this name
  hero_name = input('What is your name, challenger? \n')
  print(f'Welcome to dragon training, {hero_name} You must defeat 3 dragons.')
  print()


  hero1 = hero.Hero(hero_name, 50)
  print(hero1)

  # Uses a while loop to keep the game running until the user dies or all dragons are defeated
  while hero1._hp > 0 and (dragon1._hp > 0 or fire_dragon1._hp > 0 or flying_dragon1._hp > 0):
    # creates list for the user to select the dragon they want to fight
    attack_options = ''
    for i, dragon_n in enumerate(dragon_list):
      attack_options += f'{i + 1}. Attack ' + str(dragon_n) + '\n'

    attack_options += 'Choose a dragon to attack: ' 
    
    user_choice = check_input.get_int_range(attack_options, 1,3)
    print()
    
    selected_dragon = dragon_list[user_choice - 1]
    # Asks the user which attack they would like to perform and then executes the attack
    user_attack = check_input.get_int_range("Attack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon:", 1,2)
  
    if user_attack == "1":
      print(hero1.basic_attack(selected_dragon))
    else:
      print(hero1.special_attack(selected_dragon))

    # if the dragon is dead, remove it from the list
    if selected_dragon._hp == 0:
      dragon_list.remove(selected_dragon)

    # if the dragon list is not empty, select a random dragon to attack
    if dragon_list:
      current_dragon = random.choice(dragon_list)
    else:
      break
    rand_int = random.randint(1,2)

    # selects a random move for the dragon to attack
    if rand_int == 1:
      print(current_dragon.basic_attack(hero1))
    else:
      print(current_dragon.special_attack(hero1))
      
    print()
    print(hero1)
    
    if hero1._hp == 0:
      break
  # Lets the user know if they won or lost
  if hero1._hp > 0:
    print()
    print('Congratulations! You have defeated all 3 dragons, you have passed the trials.')
  else:
    print()
    print('Game over. You ran out of hp.')
    

main()