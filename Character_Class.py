import characterBank
import random
class Character():
    '''This is the blueprint for the characters'''

    #constructor
    def __init__(self, power, sp_power, speed):

        #defining the default attributes
        self._health = 100
        self._power = power
        self._sp_power = sp_power
        self._speed = speed
        self._type = "Human" #Using Human as unassigned
        self._name = ""

    def Report(self):
        #Returns info that was kept in a dictionary
        return{"Type": self._type,"Name": self._name, "Health": self._health, "Power": self._power, "Special Attack Power": self._sp_power, "Speed": self._speed}

    def NameC(self):
        characters = characterBank.characterBank
        x = False
        w = 0
        z = ""
        name = []
        while not x:
            y = random.randint(0,40)
            for i in characters:
                if w == y:
                    z = i
                else:
                    w = w + 1
            
            name.append(z)
            if len(name) < 5:
                name.append("-")

            elif len(name) == 5:
                x = True

        return "".join(name)
