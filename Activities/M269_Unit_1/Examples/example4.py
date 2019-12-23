#!/usr/bin/env python3

def max2(x, y):
    z = x
    if x < y:
        z = y
    return z

def greeting():
    print('Greetings Earthlings!')
    
def rotateItemsRight(aList):
    lastIndex = len(aList) - 1
    storeLast = aList[lastIndex]
    
    i = lastIndex
    while i > 0:
        aList[i] = aList[i - 1]
        i = i - 1
        
    aList[0] = storeLast
    
def max3(w, x, y):
    z = max2(x, y)
    return max2(z, w)

def stars(n):
    if n == 1:
        return '*'
    else:
        return stars(n - 1) + '*'





