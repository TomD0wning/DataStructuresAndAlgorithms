#!/usr/bin/env python3
import time

aList = [1, 2, 54, 96, 31, 305, 232, 3023492, 3243, 22, 3, 12, 2345,64,23421,9862,9076523,1144,65,19,8,55,34,29,163578,789641,3984841,1000000,101010101]

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


print("Bubblesort ",bubbleSort(aList))


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


print("ShortBubblesort ",shortBubblesort(aList))



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

print("SelectionSort ",selectionSort(aList))

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

print("IterationSort ",iterationSort(aList))


def mergeSort(aList):
    start = time.time()
    # print("Splitting ", aList)
    if len(aList) > 1:
        mid = len(aList)//2
        leftHalf = aList[:mid] #note that the python slice operator is O(k) where k is the list size
        rightHalf = aList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                aList[k]=leftHalf[i]
                i=i+1
            else:
                aList[k]=rightHalf[j]
                j=j+1
            k=k+1
        while i<len(leftHalf):
            aList[k]=leftHalf[i]
            i=i+1
            k=k+1
        while j<len(rightHalf):
            aList[k]=rightHalf[j]
            j=j+1
            k=k+1
    # print("Merging ", aList)

    end = time.time()
    return aList, end-start


print("MergeSort ", mergeSort(aList))
                    