#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

def truthTableAnd():
    t = '\t' # tab character
    print('p', t, 'q' ,t, 'p and q')
    for p in [False, True]:
        for q in [False, True]:
            print(p, t, q, t, p and q)

def truthTableOr():
    t = '\t' # tab character
    print('p', t, 'q' ,t, 'p or q')
    for p in [False, True]:
        for q in [False, True]:
            print(p, t, q, t, p or q)

def truthTableNot():
    t = '\t' # tab character
    print('p', t, 'not p')
    for p in [False, True]:
        print(p, t, not p)

def truthTableImplies():
    t = '\t' # tab character
    print('p', t, 'q' ,t, 'p --> q')
    for p in [False, True]:
        for q in [False, True]:
            print(p, t, q, t, (p and q) or not p)


truthTableAnd()
truthTableOr()
truthTableNot()
truthTableImplies()
