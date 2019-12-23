#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 19/1/13

from BinaryTree import BinaryTree

#Function to convert from node and reference
#to list of lists representation.
def makeLists(tr):
    #If tree is empty the list is empty
    if tr == None:
        return []
    #Otherwise call the function recursively
    else:
        return [tr.getRootVal(), makeLists(tr.getLeftChild()), makeLists(tr.getRightChild())]

#Level 0
t1 = BinaryTree(9)

#Level 1
t1.insertLeft(26)
t1.insertRight(18)

#Level 2
t1.getLeftChild().insertLeft(44)
t1.getLeftChild().insertRight(77)
t1.getRightChild().insertLeft(31)
t1.getRightChild().insertRight(93)

#Level 3
t1.getLeftChild().getLeftChild().insertLeft(55)

#Display list of lists representation
print(makeLists(t1))

#Function to count nodes
def nodeCount(tr):
    if tr == None:
        return 0
    else:
        return 1 + nodeCount(tr.getLeftChild()) + nodeCount(tr.getRightChild())
    
#Display node count
print('Node count:', nodeCount(t1))

#Function to count levels
def levelCount(tr):
    if tr == None:
        return 0
    else:
        return 1 + max(levelCount(tr.getLeftChild()), levelCount(tr.getRightChild()))
    
#Display level count
print('Level count:', levelCount(t1))