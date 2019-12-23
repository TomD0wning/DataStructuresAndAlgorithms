#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

import time

def exponentiation(base, exp):
    start = time.time()
    result = base
    for i in range(1, exp):
        print("test")
        result = result * base
    elapsed = time.time() - start
    print(elapsed)
    return result


print(exponentiation(7, 5))
