#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 21/4/13

from BinarySearchTree import BST, TreeNode

#Write the inorder() function here










aBST = BST()
aBST.insertNode(34, 'Fred')
aBST.insertNode(12, 'Bill')
aBST.insertNode(41, 'Jim')
aBST.insertNode(9, 'Sue')
aBST.insertNode(32, 'Ali')
aBST.insertNode(36, 'Megan')
aBST.insertNode(92, 'Roisin')
aBST.insertNode(4, 'Thibault')
aBST.insertNode(10, 'Osian')
aBST.insertNode(55, 'Niamh')
aBST.insertNode(97, 'Tudor')

inorder(aBST.root)
