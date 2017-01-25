from Character_Class import *

class Wizard(Character):
    '''This is a child class of Character'''
    #constructor
    def __init__(self):
        super().__init__(50, 70, 30)
        self._type = "Wizard"
        self._name = self.NameC()
