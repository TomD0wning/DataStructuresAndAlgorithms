"""
Code file for M269 19J TMA02 Question 2

Student version 1: 6/6/19
"""

from TMA02_Q2_BST import BST, TreeNode

class Bibliography:

    def __init__(self):
        self.bibtree = BST()

    def getReference(self,key):
        """Return the reference for the key, if it exists, otherwise None."""
        theValue = self.bibtree.retrieveKey(key,self.bibtree.root)
        if theValue == None:
            return None
        else:
            return theValue.payload

    def addReference(self, key, value):
        """Add the reference represented by key and value.

        Assume the key does not exist in the bibliography.
        """
        self.bibtree.insertNode(key,value)

    def removeReference(self, key):
        """Remove the reference with this key.

        Assume the key exists in the bibliography.
        """
        self.bibtree.deleteNode(key)

    def outputBibliography(self):
        """Return a string with all references in alphabetical order.

        There must be an empty line after each reference.
        """
        return self.traverse(self.bibtree.root)

    def traverse(self, aNode):
        """Return a string with the references in the subtree rooted at aNode.

        The references should be ordered alphabetically,
        with an empty line after each reference
        and a space between each key and its value. See the test file.
        """
        if aNode != None:
            self.traverse(aNode.hasLeftChild())
            print(aNode.key, ' ', self.bibtree.retrieveNode(aNode.key), '\n')
            self.traverse(aNode.hasRightChild())