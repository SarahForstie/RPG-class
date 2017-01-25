from Character_Class import *

class Knight(Character):
    '''This is a child class of Character'''
    #constructor
    def __init__(self):
        super().__init__(60, 10, 60)
        self._type = "Knight"
        self._name = self.NameC()
