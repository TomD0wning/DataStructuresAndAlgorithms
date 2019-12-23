#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 4/10/13

from pythonds.trees import GeneralTree
from pythonds.graphs import PriorityQueue

#Create and populate the game tree
gameTree = GeneralTree('S1', 0)
gameTree.insertChildOf('S1', 'S2', 16)
gameTree.insertChildOf('S1', 'S3', 21)
gameTree.insertChildOf('S1', 'S4', 4)
gameTree.insertChildOf('S2', 'S5', 5)
gameTree.insertChildOf('S2', 'S6', 12)
gameTree.insertChildOf('S3', 'S7', 14)
gameTree.insertChildOf('S3', 'S8', 2)
gameTree.insertChildOf('S4', 'S9', 8)
gameTree.insertChildOf('S4', 'S10', 3)
gameTree.insertChildOf('S5', 'S11', 6)
gameTree.insertChildOf('S10', 'S12', 32)


def breadthFirstSearch(aTree):
    queue = []
    queue.append(aTree.getRoot())
    while len(queue) > 0:
        printQueue(queue)
        nextNode = queue.pop(0)
        print('Visiting: ', nextNode.getKey(), '(', nextNode.getPayload(), ')', sep = '')
        children = nextNode.getChildren()
        for child in children:
            queue.append(child)
    printQueue(queue)


#Helper function for breadthFirstSearch()
def printQueue(aQueue):
    print('aQueue: [', end = '')
    if len(aQueue) > 0:
        for item in aQueue[:-1]:
            print(item.getKey(), '(', item.getPayload(), '), ', sep = '', end = '')
        lastItem = aQueue[len(aQueue) - 1]
        print(lastItem.getKey(), '(', lastItem.getPayload(), ')', sep = '', end = '')
    print(']')
    print()



#Write your bestFirstSearch() function here
#def bestFirstSearch(aTree):


#Write your bestFirstSearchRecursive() function here
#def bestFirstSearchRecursive(pQueue):

#Helper function for bestFirstSearch() and bestFirstSearchRecursive()
def printPriorityQueue(aPQueue):
    aList = aPQueue.getEntries()
    print('pQueue: [', end = '')
    if not aPQueue.isEmpty():
        for item in aList[:-1]:
            print(item[1].getKey(), '(', item[0], '), ', sep = '', end = '')
        lastItem = aList[len(aList) - 1]
        print(lastItem[1].getKey(), '(', lastItem[0], ')', sep = '', end = '')
    print(']')
    print()



#Test the functions

print('------Testing breadthFirstSearch()------')
breadthFirstSearch(gameTree)
print()


print('------Testing bestFirstSearch()------')
#Uncomment the next line to test bestFirstSearch()
#bestFirstSearch(gameTree)
print()


print('------Testing bestFirstSearchRecursive()------')
thePQueue = PriorityQueue()
thePQueue.enqueue((gameTree.getRoot().getPayload(), gameTree.getRoot()))
#Uncomment the next line to test bestFirstSearchRecursive()
#bestFirstSearchRecursive(thePQueue)
