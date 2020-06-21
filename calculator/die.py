from random import randint
from math import floor

class Die(object):
    'Die class to create different dice'

    def __new__(cls,sides):
        try:
            sides=floor(int(sides))
        except:
            print("not valid input for creating die: ",sides)
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

    def rollDie(self):
        try:
            sides=self.sides
        except:
            del self
        else:
            return randint(1,sides)

def rollD10():
    die=Die(10)
    return die.rollDie()

def rollD6():
    die=Die(6)
    return die.rollDie()

def rollXDY(count,sides):
    try:
        die=Die(sides)
        result=[]
        for throw in range(0, count):
            result.append(die.rollDie())
        return result
    except:
        print("not a proper dice")

def getXfromY(X,Y,best=True):
    try:
        if(X>len(Y)):
            raise ValueError
    except:
        print("asked more values than available")
        return 0
    else:
        if(best==True):
            Y.sort(reverse=True)
        else:
            Y.sort()
        return Y[:X]
   
        
def getXfromRolls(X,rolls,sides,best=True):
    try:
        if(X>rolls):
            raise ValueError
    except:
        print("asked more values than number of dices")
        return 0
    else:
        try:
            rolled=rollXDY(rolls,sides)
            return getXfromY(X,rolled,best)
        except:
            print("error in rolling")
        
def bestXfromRolls(X,rolls,sides):
    return getXfromRolls(X,rolls,sides,True)
    
def worstXfromRolls(X,rolls,sides):
    return getXfromRolls(X,rolls,sides,False)

            
