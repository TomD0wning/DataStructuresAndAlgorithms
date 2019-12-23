#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 21/4/13


def fibonacci(n):
    numToPrint = 0
    nextNum = 1
    for i in range(0, n):
        print(numToPrint, end=' ')
        temp = numToPrint
        numToPrint = nextNum
        nextNum = temp + nextNum



#Call the function
fibonacci(20)
