#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 09/12/13



# Helper function for hashMidSquare(). The function
# returns the middle two digits of its argument if the
# argument has an even number of digits, otherwise it
# returns the single middle digit.
def getMiddle(aNumber):
    numString = str(aNumber)
    midPoint = len(numString) // 2
    if (len(numString) % 2) == 0:
        middle = int(numString[midPoint - 1:midPoint + 1])
    else:
        middle = int(numString[midPoint])
    return middle


def hashMidSquare(aNumber, tableSize):
    numberSquared = aNumber * aNumber
    midSequence = getMiddle(numberSquared)
    hashNumber = midSequence % tableSize
    return hashNumber

#Helper function for storeIntegers().
#Returns a list of tableSize items
#all of which are None
def getNewHashTable(tableSize):
    table = []
    for i in range(0, tableSize):
        table.append(None)
    return table



def storeIntegers(intList, tableSize):
    hashTable = getNewHashTable(tableSize)
    collisions = 0
    for i in intList:
        slot = (hashMidSquare(i, tableSize))
        if hashTable[slot] != None:
            collisions = collisions + 1
            print('collision, number at slot', slot, 'will be overwritten')
        hashTable[slot] = i
    print(collisions, 'collisions occurred')
    return hashTable

#Test code for storeIntegers()
aList = list(range(50))
print(storeIntegers(aList, 100))
