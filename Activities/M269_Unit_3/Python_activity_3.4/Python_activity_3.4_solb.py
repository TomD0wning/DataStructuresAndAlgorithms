#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 20/11/12

callTotal = 0 #global variable

def sumOddNumbers(n):
    global callTotal  #Needed to modify global variable callTotal
    callTotal = callTotal + 1
    thisCall = callTotal
    print('Call', thisCall, 'of function', 'and n =', n)
    assert n > 0
    if n == 1:
        print('Base case reached, so begin to unwind, returning', 1, 'to call', thisCall - 1)
        return 1
    else:
        partialSum = sumOddNumbers(n - 1)
        if thisCall - 1 == 0:
            print('unwinding,', 'call', thisCall, 'returning the result of', ((n * 2) - 1), '+', partialSum)
        else:
            print('unwinding,', 'call', thisCall,  'returning the result of', ((n * 2) - 1), '+', partialSum, 'to call', thisCall - 1)
        return ((n * 2) - 1) + partialSum
        
print(sumOddNumbers(5)) 