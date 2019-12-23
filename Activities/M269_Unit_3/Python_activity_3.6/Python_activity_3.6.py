#!/usr/bin/env python3

# The mergeSort() and quickSort() functions are those found in Listing 5.14 
# and Listing 5.15 in Introduction to Data Structures and Algorithms in Python,
# by Bradley N. Miller, David L. Ranum. Copyright 2005.

#Authors: M269 Module Team
#Date: 20/12/12

import random
import time
from copy import copy


def mergeSort(aList):    
    if len(aList) > 1:
        mid = len(aList) // 2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                aList[k] = leftHalf[i]
                i = i + 1
            else:
                aList[k] = rightHalf[j]
                j = j + 1
            k = k + 1
        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i = i + 1
            k = k + 1 
        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j = j + 1
            k = k + 1    
    
    
    
    

def quickSort(aList):
    quickSortHelper(aList, 0, len(aList) - 1)

def quickSortHelper(aList, first, last):
    if first < last:
        splitPoint = partition(aList, first, last)
        quickSortHelper(aList, first, splitPoint - 1)
        quickSortHelper(aList, splitPoint + 1, last)

def partition(aList, first, last):
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






#Create an unsorted list of random integers to use as the argument to the above functions

list1 = []
for i in range(1, 4001):
    list1.append(random.randrange(1, 4001))


#Now lets see how the functions work with an unsorted list 
print('*** Testing the functions with a random unsorted list of integers ***')

print('mergeSort()')
start = time.time()
mergeSort(copy(list1))
end = time.time()
print('List sorted in', (end - start), 'seconds')
print()


print('quicksort()')
start = time.time()
quickSort(copy(list1))
end = time.time()
print('List sorted in', (end - start), 'seconds')



