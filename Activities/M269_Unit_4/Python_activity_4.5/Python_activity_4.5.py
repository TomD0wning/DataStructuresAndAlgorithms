#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 09/12/13

# Helper function for hashFold(). The function
# splits its integer argument into pairs of
# digits which are returned in a list.
def chopIntoPairs(aNumber):
    numString = str(aNumber)
    pairs = []
    for i in range( 0,len(numString), 2):
        pairs.append(int(numString[i: i + 2]))
    return pairs


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



# Write your functions here:

def hashFold(num, tableSize):
    sum = 0
    splitNum = chopIntoPairs(num)
    for p in range(len(splitNum)):
        sum = sum + splitNum[p]
    
    return sum%tableSize


def hashMidSquare(num, tableSize):
    return (getMiddle((num*num))%tableSize)




# Code to test the functions
print(hashFold(1459862903, 23))
print(hashMidSquare(1459862903, 23))
