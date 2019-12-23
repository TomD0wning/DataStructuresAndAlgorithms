#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 20/11/12

import random

callTotal = 0 #global variable

def recursiveInsertionSort(aList, startPosition):
    global callTotal  #Needed to modify global variable callTotal
    callTotal = callTotal + 1
    thisCall = callTotal
    print('Call', thisCall, 'of function', 'and startPosition =', startPosition)
    if startPosition == 0: #there is only 1 item in the sorted part of the list so function call ends
        print('Base case reached, so begin to unwind:')
        print('unwinding,', 'when call', thisCall, 'ends sorted part =', aList[0:startPosition + 1], 'unsorted part =', aList[startPosition + 1: len(aList)])
    else:
        recursiveInsertionSort(aList, startPosition - 1)
        currentValue = aList[startPosition]
        position = startPosition
        while position > 0 and aList[position - 1 ] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = currentValue
        print('unwinding,', 'when call', thisCall, 'ends sorted part =', aList[0:startPosition + 1], 'unsorted part =', aList[startPosition + 1: len(aList)])






#Create an unsorted list of random integers to use as the argument to the above function
list1 = []
for i in range(20):
    list1.append(random.randrange(1, 101))
    
recursiveInsertionSort(list1, len(list1) - 1)
print(list1)
