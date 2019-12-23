#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 21/1/13
#Modified: 16/12/15

from BinaryHeap2 import BinaryHeap2

myHeap = BinaryHeap2()
myHeap.insert([5, 'Clean bathroom'])
myHeap.insert([3, 'Read email'])
myHeap.insert([4, 'Water plants'])
myHeap.insert([6, 'Phone dentist'])
myHeap.insert([1, 'Feed cat'])
myHeap.insert([2, 'Check weather forecast'])

print('To do list:')
while (myHeap.size() > 0):
    print(myHeap.delMin()[1])




