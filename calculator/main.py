import dice


        
D6 = dice.Dice(6)
print (D6.showNumberOfSides())
print (D6.rollDice())

Dtesti = dice.Dice("A#")

if(Dtesti):
    print (Dtesti.showNumberOfSides())


Dtesti2 = dice.Dice(-3)

if(Dtesti2):
    print (Dtesti2.rollDice())
