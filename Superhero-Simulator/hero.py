from argparse import ArgumentError
from unicodedata import name
import random
from armor import Armor
from ability import Ability



class Hero:     #defining superhero name and hp and starting hp

    def __init__(self, name = "Kiwi", start_hp = 100):

        self.name = name

        self.hp = start_hp

        self.current_hp = start_hp

    def battle(self, opponent):

        hero_names = []
        hero_names.append (self.name)
        hero_names.append (opponent.name)

        winner = random.choice (hero_names)
        for hero in hero_names:
            if hero != winner:
                loser = hero
        print(f"Hero {loser} has been defeated by {winner}")
    
    
    self.abilities = []

    self.armory = []

    def attack(self):
        attack_value = 0
        for 

    


  
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner, print the name of the victor
  # Hint: Look into random library, more specifically the choice method

    if __name__ == "__main__":       #start testing Diego superhero

            diegos_hero = Hero("Diego Crusher", 100)

    print(diegos_hero.name)
    
    print(diegos_hero.current_hp)

Hero1 = Hero()
Hero2 = Hero("Kevchode", 150)

Hero1.battle(Hero2)





