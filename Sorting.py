#!/usr/bin/env python3
import time

def bubbleSort(aList):
    start = time.time()
    for x in range(len(aList)-1, 0, -1):
        for i in range(x):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
    end = time.time()
    return aList, end - start


print("Bubblesort ",bubbleSort([1, 2, 54, 96, 31, 305, 232, 3023492, 3243, 22, 3, 12, 2]))


def shortBubblesort(aList):
    start = time.time()

    exchanges = True
    x = len(aList)-1
    while x > 0 and exchanges:
        exchanges = False
        for i in range(x):
            if aList[i] > aList[i+1]:
                exchanges = True
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
        x = x - 1
    end = time.time()
    return aList, end - start


print("ShortBubblesort ",shortBubblesort([1, 2, 54, 96, 31, 305, 232, 3023492, 3243, 22, 3, 12, 2]))



def selectionSort(aList):
    start = time.time()
    for x in range(len(aList)-1,0,-1):
        max = 0
        for element in range(1,x+1):
            if aList[element]>aList[max]:
                max = element
        temp = aList[x]
        aList[x] = aList[max]
        aList[max] = temp
    end = time.time()
    return aList, end - start

print("SelectionSort ",selectionSort([1, 2, 54, 96, 31, 305, 232, 3023492, 3243, 22, 3, 12, 2]))

def iterationSort(aList):
    start = time.time()
    for index in range(1,len(aList)):
        currentValue = aList[index]
        position = index

        while position>0 and aList[position-1]>currentValue:
            aList[position]=aList[position-1]
            position = position-1
        aList[position]=currentValue
    end = time.time()
    return aList, end-start

print("IterationSort ",iterationSort([1, 2, 54, 96, 31, 305, 232, 3023492, 3243, 22, 3, 12, 2]))
