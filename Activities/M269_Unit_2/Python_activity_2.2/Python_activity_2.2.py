#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

from Stack import Stack

# Create a stack
myStack = Stack()

# Push items on to the stack
myStack.push(43)
myStack.push(71)
myStack.push(16)
myStack.push(27)


def displayStack(aStack):

    stackCopy = Stack()

    for x in range(aStack.size()):
        a = aStack.pop()
        print(a)
        stackCopy.push(a)
    for y in range(stackCopy.size()):
        a = stackCopy.pop()
        aStack.push(a)

# Uncomment the line below to call displayStack()
displayStack(myStack)
