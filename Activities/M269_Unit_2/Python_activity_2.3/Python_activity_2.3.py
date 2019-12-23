#!/usr/bin/env python3

# Stack class and parChecker() function by Bradley N. Miller, David L. Ranum 
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005



class Stack:
        
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    

# displayStack() function
# Authors: M269 Module Team
# Date: 20/11/12

def displayStack(aStack):
    stackCopy = Stack()
    for x in range (aStack.size()):
        stackItem = aStack.pop()
        print('    ', stackItem)
        stackCopy.push(stackItem)
    print('=============')
    for y in range (stackCopy.size()):
        stackItem = stackCopy.pop()
        aStack.push(stackItem)



    
def parChecker(symbolString):
    theStack = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(' :
            print('Symbol ' + str(index + 1) + ' is ( so pushing it on to the stack')
            theStack.push(symbol)
            print('Stack is now:')
            displayStack(theStack)
        else:
            print('Symbol ' + str(index + 1) + ' is )', end = ' ')
            if theStack.isEmpty() :
                print('but stack is empty, so expression is unbalanced')
                balanced = False                
            else:
                print('and stack not empty, so popping the stack')
                theStack.pop()
                print('Stack is now:')
            displayStack(theStack)
        index = index + 1
    print('All symbols parsed, so return result', end = ' ')
    if balanced and theStack.isEmpty() :
        return True
    else:
        return False
    

# Print the result of calling parChecker()
#print(parChecker('('))
#print(parChecker(')'))
#print(parChecker('()()())'))
#print(parChecker('((((()))))'))



