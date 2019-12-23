#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

import time

# readFile() reads a file of surnames in alphabetical order
# and returns it as a list
def readFile():
    theList = []
    file = open('surnames.txt')
    for line in file:
        theList.append(line.strip())
    return theList
    
def findName(nameToFind):
    surnames = readFile() # surnames is now a list holding a 1000 surnames
    found = False
    start = time.time()
    
    # Your code to complete the function goes here
    







# Code to test findName()
print(findName('ABBOTT'))
print()
print(findName('JOYCE'))
print()
print(findName('ZUNIGA'))
print()
print(findName('KINGSLEY')) # Not in the the list of surnames
print()


