#Binary tree, created using a list of lists approach

#function to create a simple node structure with a node & two children
def BinaryTree(r):
    return [r,[],[]]

#Function to insert a new node into the left position of a node
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

#Function to insert a new node into the left position of a node
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[], t])
    else:
        root.insert(2,[newBranch, [], []])
    return root

#Functions to access nodes in the tree
def getRootVal(root):
    return root[0]

def setRootVal(root, val):
    root[0] = val

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
print(r)
insertLeft(r,4)
print(r)
insertLeft(r,5)
print(r)
insertRight(r,6)
print(r)
insertRight(r,7)
print(r)



