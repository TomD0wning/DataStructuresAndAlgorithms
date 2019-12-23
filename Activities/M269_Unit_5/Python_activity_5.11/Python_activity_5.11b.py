#!/usr/bin/env python3

# Dynamic programming for Levenshtein edit distance.
# Straightforward algorithm, doesn't print edit steps.

# Authors: M269 Module Team
# Date: 13/06/15

# diff function
def diff(a,b):
    if a == b:
        return 0
    else:
        return 1

# Main algorithm
def editDistance(x,y):

    m = len(x)
    n = len(y)

    # Set up table, intially filled with zeros
    e = [[0 for i in range(m+1)] for j in range(n+1)]

    # Fill in table borders: these represent the simplest subproblems
    for i in range(0,n+1):
        e[i][0] = i
    for j in range(0,m+1):
        e[0][j] = j

    # Now apply dynamic programming algorithm!
    for i in range(1,n+1):
        for j in range(1,m+1):
            # match/replace, delete, insert
            e[i][j] = min(
                    e[i-1][j-1] + diff(x[j-1],y[i-1]),
                    1 + e[i-1][j],
                    1 + e[i][j-1])
    return e

# Helper function to display results
def printTable(table):
    for row in table:
        for item in row:
            print(str(item).ljust(2),end=' ')
        print()
    r = len(table)-1
    c = len(table[r])-1
    distance = str(table[r][c])
    print('Edit distance = ' + distance)
    print()
        
# Example pairs of words
str1 = 'TREES'
str2 = 'FOREST'

str3 = 'POLYNOMIAL' 
str4 = 'EXPONENTIAL'

str5 = 'KITTEN'
str6 = 'SITTING'

str7 = 'SIX'
str8 = 'ELEVEN'

e = editDistance(str1,str2)
print(str1,'to',str2)
printTable(e)

e = editDistance(str3,str4)
print(str3,'to',str4)
printTable(e)

e = editDistance(str5,str6)
print(str5,'to',str6)
printTable(e)

e = editDistance(str6,str5)
print(str6,'to',str5)
printTable(e)
    
e = editDistance(str7,str8)
print(str7,'to',str8)
printTable(e)