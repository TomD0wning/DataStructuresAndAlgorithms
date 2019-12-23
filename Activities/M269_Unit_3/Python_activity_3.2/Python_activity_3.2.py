#!/usr/bin/env python3


# The listSum() function from Listing 4.2 in
# Introduction to Data Structures and Algorithms in Python,
# by Bradley N. Miller, David L. Ranum. Copyright 2005.

#Authors: M269 Module Team
#Date: 20/11/12

import random

callTotal = 0 #global variable

def listSum(numList):
    global callTotal  #Needed to modify global variable callTotal
    callTotal = callTotal + 1
    thisCall = callTotal
    print('Call', thisCall, 'of function', 'with numList =', numList)
    if len(numList) == 1:
        print('Base case reached, so begin to unwind, returning', numList[0], 'to call', thisCall - 1)
        return numList[0]
    else:
        sumOfSublist = listSum(numList[1:])
        result = numList[0] + sumOfSublist
        if thisCall - 1 == 0:
            print('unwinding,', 'call', thisCall, 'returning the result of', numList[0], '+', sumOfSublist)
        else:
            print('unwinding,', 'call', thisCall,  'returning the result of', numList[0], '+', sumOfSublist, 'to call', thisCall - 1)
        return result


#Create a list of random integers to use as the argument to listSum()
list1 = []
for i in range(1, 6):
    list1.append(random.randrange(1, 11))
    
#Test the function
print(listSum(list1))