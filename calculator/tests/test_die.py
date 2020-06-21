import pytest
import die
from math import floor

def test_correctConstruction():
    sides=6
    D6=die.Die(sides)
    assert sides == D6.showNumberOfSides()

def test_correctConstructionWithAlphaInput():
    sides="10"
    D10=die.Die(sides)
    assert int(sides) == D10.showNumberOfSides()
    

def test_incorrectConstructionNonNumber():
    sides="a"
    Da=die.Die(sides)
    notExist = False
    if not Da:
        notExist = True
    assert True == notExist

def test_incorrectConstructionEmpty():
    sides=""
    D=die.Die(sides)
    notExist = False
    if not D:
        notExist = True
    assert True == notExist

    
def test_incorrectConstructionZero():
    sides=0
    D0=die.Die(sides)
    notExist = False
    if not D0:
        notExist = True
    assert True == notExist

def test_incorrectConstructionNegative():
    sides=-10
    Dminus=die.Die(sides)
    notExist = False
    if not Dminus:
        notExist = True
    assert True == notExist

def test_rollD6():
    for i in range(1,100):
        roll=die.rollD6()
        assert roll>0
        assert roll<7
    
       
def test_rollD10():
    for i in range(1,100):
        roll=die.rollD10()
        assert roll>0
        assert roll<11

def test_roll5D10():
    rolls=die.rollXDY(5,10)
    assert len(rolls)==5
    for roll in rolls:
        assert roll>0
        assert roll<11

def test_best():
    X=4
    Y=[2,3,1,4,15,163,3,134,163]
    result=die.getXfromY(X,Y)
    correct=[15,163,134,163]
    assert result.sort()==correct.sort()
        
def test_worst():
    X=1
    Y=[1,4,45,1,4,1,534512,543,4,1]
    result=die.getXfromY(X,Y,False)
    assert result==[1]
