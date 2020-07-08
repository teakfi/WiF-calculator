# -*- coding: utf-8 -*-
"""
Nuclear research for World in Flames

Created on Fri Jul  3 16:50:25 2020

number of turns = number of times the nuclear research rolls are done

@author: tuokall
"""

import die
import math

def rollRun(target,numberOfTrials,turns, rolls,start):
    successCount=0
    i=0
    while(i < numberOfTrials):
        sum=start
        rollcount=0
        for turn in range(turns):
            sum+=die.bestXfromRolls(1, rolls, 10)[0]
            
        if(sum>=target):
            successCount+=1
        i+=1    
        
    return successCount


def rollRunToGetCert(target,turns,certainty,start):
    rolls=1
    while(True):
        numberOfTrials=5000
        successCount=rollRun(target,numberOfTrials,turns,rolls,start)
            
        if(successCount/numberOfTrials>certainty):
            break
        else:
            rolls+=1

    return rolls,successCount/numberOfTrials
    
def simpleHowToGet(target, turns, certainty=0.95, start=0):
    try:
        if((target-start)/turns>10):
            raise ValueError
    except:
        print('Not possible to achieve result {0} with starting value {1} in {2} turns'.format(target,start,turns))
        return 0
    else:
        return rollRunToGetCert(target,turns,certainty,start)
    

def howToGet(target, turns, certainty=0.95, start=0):
    high, origcert=simpleHowToGet(target, turns, certainty, start)
    low = high - 1
    changeturn=turns//2
    change=changeturn
    while(True):
        numberOfTrials=5000
        i=0
        successCount=0
        while(i < numberOfTrials):
            sum=start
            for turn in range(changeturn):
                sum+=die.bestXfromRolls(1, high, 10)[0]
            for turn in range(changeturn, turns):
                sum+=die.bestXfromRolls(1, low, 10)[0]
            if(sum>=target):
                successCount+=1
            i+=1
        runcertainty=successCount/numberOfTrials
        if(math.isclose(runcertainty,certainty,abs_tol=0.001)):
            break
        if(change==1):
            break
        change=change//2
        if(runcertainty>certainty):
            changeturn-=change
        else:
            changeturn+=change
    return high, low, changeturn
    


#testing

print(simpleHowToGet(101, 10))
print(simpleHowToGet(100,15))
print(simpleHowToGet(100, 15,0.5))
print(howToGet(100,15))

