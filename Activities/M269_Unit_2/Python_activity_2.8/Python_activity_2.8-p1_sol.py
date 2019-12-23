#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

import time

def readFile():
    theList = []
    file = open('surnames.txt')
    for line in file:
        theList.append(line.strip())
    return theList
    
def findName(nameToFind):
    surnames = readFile()
    found = False
    start = time.time()
    for name in surnames:
        if nameToFind == name:
            found = True
            break
    elapsed = (time.time() - start)
    print(elapsed)
    print('milliseconds to search for ' + nameToFind)
    return found
    
print(findName('ABBOTT'))
print()
print(findName('JOYCE'))
print()
print(findName('ZUNIGA'))
print()
print(findName('KINGSLEY')) # Not in the the list of surnames
print()
