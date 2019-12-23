#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

def exponentiation(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = result * base
        base = base * base
        exp = exp // 2
    return result
 
# Print the result of calling the function   
print(exponentiation(4, 7))
