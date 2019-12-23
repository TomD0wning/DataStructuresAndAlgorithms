#!/usr/bin/env python3

# Implementation of a General Tree

#M269 module team
#version 1.0 15/08/13



# ========== CLASS GeneralTree ==================

class GeneralTree:

# --------- PUBLIC METHODS ----------

#   Constructor
    def __init__(self, key, pay):
        self.root = GTreeNode(key, pay)

    def getRoot(self):
        return self.root

#   Insert a node as child of node with key specified
    def insertChildOf(self, parentKey, newKey, newPay):
        parentNode = self.findNode([self.root], parentKey)
        if parentNode:
            newTree = GTreeNode(newKey, newPay)
            newTree.parent = parentNode
            parentNode.children.append(newTree)
        else:
            print('Specified parent node is not in tree')


#   Delete a node with the supplied key
    def deleteNode(self, key):
        delNode = self.findNode([self.root], key)
        if delNode:
            if delNode.parent == None:
                print('Deleting root')
                self.root = delNode.children[0]
                self.root.children = delNode.children[1:] + delNode.children[0].children
            else:
                print('Deleting node ', key)
                for child in delNode.children:
                    child.parent = delNode.parent
                delNode.parent.children = delNode.parent.children + delNode.children
                delNode.parent.children.remove(delNode)
        else:
            print('Specified node is not in the tree')


#   Return the node with supplied key
    def getNode(self, key):
        return self.findNode([self.root], key)


#   Print tree with indentation
    def printTree(self):
        self.printDFS(self.root, '')


# --------- INTERNAL METHODS ----------

#   Finds a node by searching tree breadth first
    def findNode(self, bFSQueue, parentKey):
        if len(bFSQueue) == 0:
            return None
        else:
            queueFront = bFSQueue.pop(0)
            if queueFront.key == parentKey:
                return queueFront
            else:
                return self.findNode(bFSQueue + queueFront.children, parentKey)


#   Prints the tree in depth first order with indentation
    def printDFS(self, node, spacer):
        print(spacer, node.key, ' ', node.payLoad)
        if len(node.children) == 0:
            return
        else:
            for child in node.children:
                self.printDFS(child, spacer + '    ')

# ========== End of CLASS GeneralTree ===========





# ========== CLASS GTreeNode ====================

class GTreeNode:

    def __init__(self, key, pay):
        self.parent = None
        self.key = key
        self.payload = pay
        self.children = []

    def getPayload(self):
        return self.payload

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def getKey(self):
        return self.key

# ========== End of CLASS GTreeNode ===========
