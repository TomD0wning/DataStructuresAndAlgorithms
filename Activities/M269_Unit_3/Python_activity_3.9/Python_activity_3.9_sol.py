#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 29/1/13

#Function to test if a list represents a heap
def isHeap(aList):
    for i in range (len(aList) - 1, 1, -1):
        if aList[i] < aList[i // 2]: 
            return False
    return True


print(isHeap([0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]))
print(isHeap([0, 9, 5, 11, 14, 18, 19, 21, 33, 17, 27]))




