#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

import time

def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n + 1) :
        theSum = theSum + i
    end = time.time()
    return theSum, end - start
        
def sumOfN3(n):
    start = time.time()
    theSum = (n * (n + 1) / 2)
    end = time.time()
    return theSum, end - start



print('Result of calling sumOfN2(50000)')
print(sumOfN2(50000))
print()

print('Result of calling sumOfN2(100000):')
print(sumOfN2(100000))
print()

print('Result of calling sumOfN2(150000):')
print(sumOfN2(150000))
print()

print('Result of calling sumOfN2(200000):')
print(sumOfN2(200000))
print()

print('Result of calling sumOfN3(50000)')
print(sumOfN3(50000))
print()

print('Result of calling sumOfN3(100000):')
print(sumOfN3(100000))
print()

print('Result of calling sumOfN3(150000):')
print(sumOfN3(150000))
print()

print('Result of calling sumOfN3(200000):')
print(sumOfN3(200000))
print()
