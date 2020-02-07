class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()

    def insertNode(self, key, value):
        if self.root:
            self.insertIn(key, value, self.root)
        else:
            self.root = TreeNode(key,value)
        self.size = self.size + 1

    def retrieveNode(self, key):
        if self.root:
            result = self.retrieveKey(key,self.root)
        if result:
            return result.payload
        else:
            return None

    def deleteNode(self, key):
        if self.size > 1:
            nodeToRemove = self.retrieveKey(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error key not in tree')

    def retrieveKey(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.retrieveKey(key, currentNode.leftChild)
        else:
            return self.retrieveKey(key, currentNode.rightChild)


    def insertIn(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.insertIn(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.insertIn(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,value, parent=currentNode)

    def remove(self, currentNode):
        if currentNode.isLeaf():   # Delete a leaf node
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            successor = currentNode.findSuccessor()
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload
        else:                      # Delete a node with one child
            if currentNode.hasLeftChild():     # The one child is a left child
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:                              # The one child is a right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

class TreeNode:

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def itLeaf(self):
        return not (self.isLeftChild and self.isRightChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,right,left):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        successor = None
        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return successor

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent