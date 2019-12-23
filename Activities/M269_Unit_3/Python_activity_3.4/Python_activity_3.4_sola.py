#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 20/11/12


def sumOddNumbers(n):
    assert n > 0
    if n == 1:
        return 1
    else: 
        return ((n * 2) - 1) + sumOddNumbers(n - 1)
        
print(sumOddNumbers(5)) 