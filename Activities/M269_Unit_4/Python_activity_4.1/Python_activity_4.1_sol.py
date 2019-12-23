#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 09/12/13
#Modified: 3/2/16

def quickSelect(k, aList):

    if len(aList) == 1:
        return aList[0]

    pivotValue = aList[0]
    leftPart = []
    rightPart = []

    for item in aList[1:]:
        if item < pivotValue:
             leftPart.append(item)
        else:
            rightPart.append(item)

    if len(leftPart) >= k:
        return quickSelect(k, leftPart)
    elif len(leftPart) == k - 1:
        return pivotValue
    else:
        return quickSelect(k - len(leftPart) -1, rightPart)



# Test the function
theList = [2, 36, 5, 21, 8, 13, 11, 20, 4, 1]
print(quickSelect(6, theList))
