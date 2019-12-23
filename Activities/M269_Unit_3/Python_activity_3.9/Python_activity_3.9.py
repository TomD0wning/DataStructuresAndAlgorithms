#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 19/1/13

from BinaryHeap import BinaryHeap

#List from Miller and Ranum Figure 6.18.

#Example 1 - adding items one at a time
myHeap = BinaryHeap()
aList = [9, 6, 5, 2, 3]
print('Example 1 - adding items one at a time')
print('List to build heap from:', aList)
print('Heap list:', myHeap.heapList)
print('-----------------------------------------')

for k in range(len(aList)):
    myHeap.insert(aList[k])
    print('-----------------------------------------')
    
print('Finished: heap is', myHeap.heapList)
print()

#Example 2 - "heapifying" an existing list
myHeap2 = BinaryHeap()
bList = [9, 6, 5, 2, 3]
print('Example 2 - heapifying an existing list')
print('List to heapify:', bList)

myHeap2.buildHeap(bList)
print('Finished')





