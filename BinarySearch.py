import time
import math
import random

#Given an array of x integers, how many iterations of a given problem definition does it take to find n where n is an integer within the given
#array. [0...400] find 3

def findTheNumber(n):
    iterationCount = 0
    numberList = list(range(0,401))
    index = 0
    start = time.time()
    while index != n:
        iterationCount+=1
        index = numberList[(len(numberList)//2)]
        numberList = splitSearchSpace(n,numberList)

    print('Success. Number of iteractions: ',iterationCount)
    print('found ',n, ' in ', time.time() - start)


#split the search space and return the section in which the value could occur, where a is the search value and b is the search space
def splitSearchSpace(a,b):
    split = b[(len(b)//2)]
    if a > split :
        print('>= n',split)
        return b[(len(b)//2):]
    else:
        print('<= n',split)
        return b[:(len(b)//2)]

# randomNumber = random.randint(0,10000001)
findTheNumber(7)