from Character_Class import *

class Barbarian(Character):
    '''This is a child class of Character'''
    #constructor
    def __init__(self):
        super().__init__(70, 20, 50)
        self._type = "Barbarian"
        self._name = self.NameC()
        
tim = Barbarian()
tim.NameC()
print(tim.Report())
