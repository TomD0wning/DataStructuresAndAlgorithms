#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 19/1/13

from BinaryTree import BinaryTree

#Create a node and reference representation of the
#tree shown in Figure 6.6(a) on p. 238 of Ranum and Miller.
#The nodes are added level by level working downwards.
print('Creating tree')
#Level 0
t = BinaryTree('a')

#Level 1
t.insertLeft('b')
t.insertRight('c')

#Level 2
t.getLeftChild().insertLeft('d')
t.getLeftChild().insertRight('e')
t.getRightChild().insertLeft('f')

#Function to convert from node and reference
#to list of lists representation.
def makeLists(tr):
    #If tree is empty the list is empty
    if tr == None:
        return []
    #Otherwise call the function recursively
    else:
        return [tr.getRootVal(), makeLists(tr.getLeftChild()), makeLists(tr.getRightChild())]
    
#Display list of lists representation
print('List of lists representation')
print(makeLists(t))


