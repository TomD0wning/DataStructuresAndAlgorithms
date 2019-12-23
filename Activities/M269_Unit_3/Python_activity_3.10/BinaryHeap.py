#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 4/6/12
#Modified: 16/12/15

class BinaryHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
       
    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2        
            
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percolateUp(self.currentSize)
        
    def minChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1
        
    def percolateDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
            
    def delMin(self):
        returnValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        print('Pop root item', returnValue, 'and move last item to root')
        print(self.heapList)
        print('Percolate down')
        print('-----------------------------------------------')
        self.percolateDown(1)
        print(self.heapList)
        print('    ^')
        return returnValue
    
    def buildHeap(self, aList):
        i = len(aList) // 2
        self.currentSize = len(aList)
        self.heapList = [0] + aList[:]
        while i > 0 :
            self.percolateDown(i)
            i = i - 1
        return self.heapList[1:len(self.heapList)]
    
    def size(self):
        return self.currentSize
