#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 20/11/12

import random

callTotal = 0 #global variable

def factorial(n):
    global callTotal  #Needed to modify global variable callTotal
    callTotal = callTotal + 1
    thisCall = callTotal
    print('Call', thisCall, 'of function', 'with n =', n)
    assert n > 0
    if n == 1:
        print('Base case reached, so begin to unwind, returning', 1, 'to call', thisCall - 1)
        return 1
    else :
        partialResult = factorial(n - 1)
        if thisCall - 1 == 0:
            print('unwinding,', 'call', thisCall, 'returning the result of', n, '*', partialResult)
        else:
            print('unwinding,', 'call', thisCall,  'returning the result of', n, '*', partialResult, 'to call', thisCall - 1)
        return n * partialResult
    
    
#Assign anInt with a random number between 5 and 10
anInt = random.randrange(5, 11)
    
#Call the function   
print(factorial(anInt))
