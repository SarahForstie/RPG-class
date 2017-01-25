from Barbarian_Class import *
from Elf_Class import *
from Wizard_Class import *
from Dragon_Class import *
from Knight_Class import *

import random

team = []
x = 0

while x < 10:
    y = random.randint(1,5)
    if y == 1:
        my_class = Barbarian()
    elif y == 2:
        my_class = Elf()
    elif y == 3:
        my_class = Wizard()
    elif y == 4:
        my_class = Dragon()
    elif y == 5:
        my_class = Knight()
        
    team.append(my_class)
    x = x+1

for i in team:
    print(i.Report())
