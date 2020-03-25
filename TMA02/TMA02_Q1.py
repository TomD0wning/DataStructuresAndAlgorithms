"""
Code file for M269 19J TMA02 Q1
Student version 1: 6/6/19
"""

import math

# This is the original selection sort code, do NOT change it

def selectionSort(alist):
    '''Sort alist in place, using selection sort.'''
    for outer in range(len(alist)):
        minPosition = outer
        for inner in range(outer+1, len(alist)):
            if alist[minPosition] > alist[inner]:
               minPosition = inner
        temp = alist[outer]
        alist[outer]= alist[minPosition]
        alist[minPosition]=temp
    return alist

# Write the function below to answer Q1 b

def selectionMedian(alist):
    '''Return the median of alist, a list of numbers.

    Assume the length of alist is odd.
    '''

    for outer in range(math.ceil(len(alist)/2)):
        minPosition = outer
        for inner in range(outer+1, len(alist)):
            if alist[minPosition] > alist[inner]:
               minPosition = inner
        temp = alist[outer]
        alist[outer]= alist[minPosition]
        alist[minPosition]=temp
    return alist[outer]

