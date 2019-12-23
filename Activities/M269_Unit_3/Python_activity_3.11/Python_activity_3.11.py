#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 23/1/13

import random
import time

n = 500000 #Length of list to be sorted.

def timTrial(c):
    #Integers 1 - n in order!
    data = list(range(1, n + 1))

    #Contaminate the list with c random swaps.
    for i in range(c):
        first = random.randint(0, n - 1)
        second = random.randint(0, n - 1)
        temp = data[first]
        data[first] = data[second]
        data[second] = temp
        
    #Time how long Timsort takes to the sort the list.
    start = time.time()
    sorted(data)
    end = time.time()
    return(end - start)

#Sorting a random permutation for comparison benchmark.
#Integers 1 - n shuffled!
data = list(range(1, n + 1))
random.shuffle(data)
start = time.time()
sorted(data)
end = time.time()
benchmark = (end - start)
print('Benchmark:', benchmark)



