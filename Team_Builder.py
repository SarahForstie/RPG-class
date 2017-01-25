from Barbarian_Class import *
from Elf_Class import *
from Wizard_Class import *
from Dragon_Class import *
from Knight_Class import *

def addCharacter(letter):
    if letter in ("B","b"):
        my_class = Barbarian()

    elif letter in ("E","e"):
        my_class = Elf()

    elif letter in ("W","w"):
        my_class = Wizard()

    elif letter in ("D","d"):
        my_class = Dragon()

    elif letter in ("K","k"):
        my_class = Knight()

    else:
        return "Not found"

    return my_class

def main():
    team = []
    done = False
    while not done:
        print("Character choices:\nBarbarian(B)\nElf(E)\nWizard(W)\nDragon(D)\nKnight(K)\n")
        character = input("What type of character do you want to add to your team(enter letter next to name)? ")
        
