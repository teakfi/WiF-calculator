import pytest
import dice
from math import floor

def test_correctConstruction():
    sides=6
    D6=dice.Dice(sides)
    assert sides == D6.showNumberOfSides()

def test_correctConstructionWithAlphaInput():
    sides="10"
    D10=dice.Dice(sides)
    assert int(sides) == D10.showNumberOfSides()
    

def test_incorrectConstructionNonNumber():
    sides="a"
    Da=dice.Dice(sides)
    notExist = False
    if not Da:
        notExist = True
    assert True == notExist

def test_incorrectConstructionEmpty():
    sides=""
    D=dice.Dice(sides)
    notExist = False
    if not D:
        notExist = True
    assert True == notExist

    
def test_incorrectConstructionZero():
    sides=0
    D0=dice.Dice(sides)
    notExist = False
    if not D0:
        notExist = True
    assert True == notExist

def test_incorrectConstructionNegative():
    sides=-10
    Dminus=dice.Dice(sides)
    notExist = False
    if not Dminus:
        notExist = True
    assert True == notExist

    
       
    
    
        

