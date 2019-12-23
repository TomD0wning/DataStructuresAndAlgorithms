#! /usr/bin/env python3

def max2(x,y):
    z = x
    if x < y:
        z=y
    return z

def rotateItemsRight(aList):

    lastIndex = len(aList) - 1

    storeLast = aList[lastIndex]

    i = lastIndex

    while i > 0:

        aList[i] = aList[i - 1]

        i = i - 1

    aList[0] = storeLast

bList = ['e', 'a', 't']

rotateItemsRight(bList)


def stars(n):

    if n == 1:

        return '*'

    else:

        return stars(n - 1) + '*'


#Activity 1.11

#1 Function mean takes two numbers as arguments and returns their mean

def findTheMean(x,y):
    return (x+y)/2

#2 Function printWithStars takes a string as an argument and prints the string between two sets of three stars

def printWithStars(inputString):
    threeStars = '***'
    return threeStars + inputString + threeStars

#3 Function isEven takes an argument which is a positive integer and returns True if the number is even, otherwise False

def isEven(n):
    if n > 0 and (n % 2 == 0):
        return True
    return False

def isEven2(n):
    return n%2 == 0

# Function triangle takes an argument which is a positive integer and prints a triangle of stars, starting with 1 star on the first line, 
# 2 on the second line, and so on, with the last line containing a number of stars equal to the argument.

def triangle(triangleDepth):
    currentDepth = 1
    while currentDepth <= triangleDepth:
        print('*'*currentDepth)
        currentDepth = currentDepth +1

def triangle2(d):
    for i in range(d+1):
        print('*'*i)

triangle2(10)

