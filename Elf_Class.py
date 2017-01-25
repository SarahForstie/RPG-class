from Character_Class import *

class Elf(Character):
    '''This is a child class of Character'''
    #constructor
    def __init__(self):
        super().__init__(30, 60, 10)
        self._type = "Elf"
        self._name = self.NameC()
