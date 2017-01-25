from Character_Class import *

class Dragon(Character):
    '''This is a child class of Character'''
    #constructor
    def __init__(self):
        super().__init__(90, 40, 50)
        self._type = "Dragon"
        self._name = self.NameC()
