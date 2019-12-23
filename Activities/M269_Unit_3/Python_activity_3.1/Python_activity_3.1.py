#!/usr/bin/env python3


# The bubbleSort(), shortBubbleSort, selectionSort() and insertionSort() functions based on those
# by Bradley N. Miller, David L. Ranum in Introduction to Data Structures and
# Algorithms in Python, Copyright 2005.

#Authors: M269 Module Team
#Date: 19/11/13


import random
import time
from copy import copy


def bubbleSort(aList):
    #print('Initial list =', aList)
    noOfSwaps = 0
    noOfAssignments = 0
    comparisons = 0
    start = time.time()
    for passNum in range(len(aList) - 1, 0, -1):
        for i in range(passNum):
            comparisons = comparisons + 1
            if aList[i] > aList[i + 1]:               
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
                noOfSwaps = noOfSwaps + 1
                noOfAssignments = noOfAssignments + 3
    elapsed = (time.time() - start)
    #print('Sorted list = ', aList)
    print('Comparisons =', comparisons)  
    print('Swaps =', noOfSwaps)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')   

def shortBubbleSort(aList):
    #print('Initial list =', aList)
    noOfSwaps = 0
    noOfAssignments = 0
    comparisons = 0
    hasSwapped = True
    passNum = len(aList) - 1
    start = time.time()
    while passNum > 0 and hasSwapped:
        hasSwapped = False
        for i in range(passNum):
            comparisons = comparisons + 1
            if aList[i] > aList[i + 1]:               
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
                noOfSwaps = noOfSwaps + 1
                noOfAssignments = noOfAssignments + 3
                hasSwapped = True
        passNum = passNum - 1
    elapsed = (time.time() - start)
    #print('Sorted list = ', aList)
    print('Comparisons =', comparisons)  
    print('Swaps =', noOfSwaps)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')    
    
    
    
def selectionSort(aList):
    #print('Initial list =', aList)
    noOfSwaps = 0
    noOfAssignments = 0
    comparisons = 0
    start = time.time()
    for j in range(len(aList) - 1, 0, -1):
        maxPos = 0
        for i in range(1, j + 1):
            comparisons = comparisons + 1
            if aList[i] > aList[maxPos]:
                maxPos = i
        temp = aList[j]
        aList[j] =  aList[maxPos]
        aList[maxPos] = temp
        noOfSwaps = noOfSwaps + 1
        noOfAssignments = noOfAssignments + 3
    elapsed = (time.time() - start)
    #print('Sorted list = ', aList)
    print('Comparisons =', comparisons)  
    print('Swaps =', noOfSwaps)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')    
    
    

def insertionSort(aList):
    #print('Initial list =', aList)
    shifts = 0
    noOfAssignments = 0
    comparisons = 0
    start = time.time()
    for i in range(1, len(aList)):
        currentValue = aList[i]
        noOfAssignments = noOfAssignments + 1
        position = i
        entered = False
        while position > 0 and aList[position - 1] > currentValue:
            entered = True
            comparisons = comparisons + 1
            aList[position] = aList[position - 1]
            shifts = shifts + 1
            noOfAssignments = noOfAssignments + 1
            position = position - 1
        aList[position] = currentValue
        noOfAssignments = noOfAssignments + 1
        if not entered:
            comparisons = comparisons + 1
    elapsed = time.time() - start
    #print('Sorted list = ', aList)
    print('Comparisons =', comparisons)  
    print('Shifts =', shifts)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')
    
    
    
    
#************* Code to test the functions ************* 

#Create an unsorted list of random integers to use as the argument to the above functions

list1 = []
for i in range(1, 4001):
    list1.append(random.randrange(1, 4001))
         


#Now lets see how the functions work with an unsorted list 
print('*** Testing the sorting functions with a random unsorted list of integers ***')         
print('bubbleSort()')
bubbleSort(copy(list1))
print()

print('shortBubbleSort()')
shortBubbleSort(copy(list1))
print()

print('selectionSort()')
selectionSort(copy(list1))
print()

print('insertionSort()')
insertionSort(list1)
print()

# list1 is now sorted
print('*** Testing the sorting functions with a sorted list of integers ***')
print('bubbleSort()')
bubbleSort(list1)
print()

print('shortBubbleSort()')
shortBubbleSort(list1)
print()

print('selectionSort()')
selectionSort(list1)
print()

print('insertionSort()')
insertionSort(list1)


