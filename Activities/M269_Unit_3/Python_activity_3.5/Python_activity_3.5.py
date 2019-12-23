#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 20/11/12

import random


def recursiveInsertionSort(aList, startPosition):
    if startPosition == 0: #there is only 1 item in the sorted part of the list so function call ends
         return
    else:
        recursiveInsertionSort(aList, startPosition - 1)
        currentValue = aList[startPosition]
        position = startPosition
        while position > 0 and aList[position - 1 ] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = currentValue





#Create an unsorted list of random integers to use as the argument to the above function
list1 = []
for i in range(20):
    list1.append(random.randrange(1, 101))
    
recursiveInsertionSort(list1, len(list1) - 1)
print(list1)