#! /usr/bin/env python3

def naturalNumbers():
    print(sum(_ for _ in range(0,1000) if( _ % 3 == 0 or _ % 5 ==0)))

# naturalNumbers


def isTrue():
    a = False
    b = True
    if(a or not b):
        print("here")

isTrue()