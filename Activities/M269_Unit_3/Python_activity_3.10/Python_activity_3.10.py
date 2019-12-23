#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 20/1/13
#Modified: 16/12/15

from BinaryHeap import BinaryHeap

#Example 1 heapsort in action
aList = [1, 9, 5, 2, 14, 4, 8, 20, 7, 42]

#First 'heapify' the list
myHeap = BinaryHeap()
myHeap.buildHeap(aList)

#Create empty list to hold the results
sortedList = []

print('The list to be sorted:', aList)
print('The heap:', myHeap.heapList)
print()

#While there are still items in the heap, pop the root and then reform the heap
while myHeap.size() > 0:
    item = myHeap.delMin()
    sortedList.append(item)

print('Finished')
print('Sorted list:', sortedList)





