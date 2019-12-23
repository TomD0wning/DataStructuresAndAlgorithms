#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

import timeit

theList = [] # global variable

def readFile():
    file = open('surnames.txt')
    for line in file:
        theList.append(line.strip())
    
def findName(nameToFind):
    surnames = theList
    found = False
    for name in surnames:
        if nameToFind == name:
            found = True
            break
    return found

readFile() # populate global variable theList

t1 = timeit.Timer("findName('ABBOTT')", "from __main__ import findName")
print (t1.timeit(number=1000))
print("seconds to search 1000 times for ABBOTT")
print()

t2 = timeit.Timer("findName('JOYCE')", "from __main__ import findName")
print (t2.timeit(number=1000))
print("seconds to search 1000 times for JOYCE")
print()

t3 = timeit.Timer("findName('ZUNIGA')", "from __main__ import findName")
print (t3.timeit(number=1000))
print("seconds to search 1000 times for ZUNIGA")
print()

t4 = timeit.Timer("findName('KINGSLEY')", "from __main__ import findName")
print (t4.timeit(number=1000))
print("seconds to search 1000 times for KINGSLEY")
print()

