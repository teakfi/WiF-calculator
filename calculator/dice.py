from random import randint
from math import floor

class Dice(object):
    'Dice class to create different dices'

    def __new__(cls,sides):
        try:
            sides=floor(int(sides))
        except:
            print("not valid input creating dice: ",sides)
        else:
            try:
                if sides<1:
                    raise ValueError
            except:
                print("Die needs to have atleast one side, input: ",sides)
            else:
                return object.__new__(cls)
                
    
    def __init__(self, sides):
        self.sides=floor(int(sides))

                
    def showNumberOfSides(self):
        try:
            sides=self.sides
        except:
            del self
        else:
            return sides

    def rollDice(self):
        try:
            sides=self.sides
        except:
            del self
        else:
            return randint(1,sides)

