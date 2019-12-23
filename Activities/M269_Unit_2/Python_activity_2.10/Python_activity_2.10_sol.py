#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12



def russianMult(x, y):
    result = 0
    while x > 0:
        if x % 2 == 1:
            result = result + y
        y = y * 2
        x = x // 2
    return result
 
# Print the result of calling the function  
print(russianMult(6, 6))

print(russianMult(4, 7))
