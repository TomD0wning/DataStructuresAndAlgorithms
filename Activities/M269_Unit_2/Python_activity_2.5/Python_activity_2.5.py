#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12



def printList(aList):
    n = 0
    while n <= len(aList):
        print(aList[n])
        n = n + 1
        
def sequentialFind(aList, item):
    n = 0
    found = False
    while n < len(aList) or not found:
        if aList[n] == item:
            found = True
        n = n + 1
    return found

# Create a list
theList = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]

# Add your function calls here



        
