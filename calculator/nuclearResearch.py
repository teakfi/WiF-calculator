# -*- coding: utf-8 -*-
"""
Nuclear research for World in Flames

Created on Fri Jul  3 16:50:25 2020

@author: tuokall
"""

import die

   
def howManyRollsInTurnToGet(target, turns, certainty=0.95, start=0):
    try:
        if((target-start)/turns>10):
            raise ValueError
    except:
        print('Not possible to achieve result {0} with starting value {1} in {2} turns'.format(target,start,turns))
        return 0
    else:
        rolls=1
        while(True):
            numberOfTrials=10000
            successCount=0
            i=0
            while(i < numberOfTrials):
                sum=start
                turn=1
                for turn in range(turns):
                    sum+=die.bestXfromRolls(1, rolls, 10)[0]
                
                if(sum>=target):
                    successCount+=1
                i+=1
            if(successCount/numberOfTrials>certainty):
                break
            else:
                rolls+=1

        return rolls,successCount/numberOfTrials
    


'''
testing

print(howManyRollsInTurnToGet(101, 10))
print(howManyRollsInTurnToGet(100,15))
print(howManyRollsInTurnToGet(100, 15,0.5))
'''
