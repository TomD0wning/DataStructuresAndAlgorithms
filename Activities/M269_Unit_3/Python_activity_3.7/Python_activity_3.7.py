#!/usr/bin/env python3

# The quickSort() function is based on that in Listing 5.15
# of Introduction to Data Structures and Algorithms in Python,
# by Bradley N. Miller, David L. Ranum. Copyright 2005.

#Authors: M269 Module Team
#Date: 14/11/13

import random
import time

def quickSort(aList):
    quickSortHelper(aList, 0, len(aList) - 1)
    

def quickSortHelper(aList, first, last):
    if first < last:
        splitPoint = partition(aList, first, last)
        quickSortHelper(aList, first, splitPoint - 1)
        quickSortHelper(aList, splitPoint + 1, last)


def partition(aList, first, last):
    
    # Random value
    # We choose a random pivot and then swap its value with the
    # value of the first item in aList. The remainder of the
    # algorithm, as usual, works with the value of first item in
    # aList as the pivot
    #pivot = random.choice(list(range(first, last + 1)))
    #temp = aList[first]
    #aList[first] = aList[pivot]
    #aList[pivot] = temp
    # Random value end

    # Median of three
    # We sort the first, middle and last items in the list into 
    # ascending order, choose the resulting middle value as the 
    # pivot and then swap its value with the value of the first 
    # item in aList. The remainder of the algorithm, as usual, 
    # works with the value of first item in aList as the pivot
    #middle = (first + last)//2
    #items = sorted([(aList[first], first), (aList[middle], middle), (aList[last], last)])
    #(pivotValue, pivot) = items[1]
    #temp = aList[first]
    #aList[first] = aList[pivot]
    #aList[pivot] = temp
    # Median of three end
    
    # First value
    pivotValue = aList[first]
   
    leftMark = first + 1
    rightMark = last
    done = False
    while not done:

        while leftMark <= rightMark and aList[leftMark] <= pivotValue:
            leftMark = leftMark + 1

        while aList[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:
            temp = aList[leftMark]
            aList[leftMark] = aList[rightMark]
            aList[rightMark] = temp

    temp = aList[first]
    aList[first] = aList[rightMark]
    aList[rightMark] = temp
    return rightMark


#Function to read numbers from a file and return as a list
def getNumbersFromFile(fileName):
    with open(fileName) as f:
        aList = [int(x) for x in f]
    f.close()
    return aList


# Change the following line to read in a different data set.
fileName = 'dataset1.txt'

list1 = getNumbersFromFile(fileName)
print('INPUT = ', list1[0:20])
start = time.time()
quickSort(list1)
end = time.time()
print('OUTPUT = ', list1[0:20])
print('List sorted in', (end - start), 'seconds')


