#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 09/12/13, 07/02/15

import time

def basicStringSearch(searchString, target):
    searchIndex = 0
    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0
        while (targetIndex < len(target)) and target[targetIndex] == searchString[targetIndex + searchIndex]:
            targetIndex = targetIndex + 1
        if targetIndex == len(target):
            return searchIndex
        searchIndex = searchIndex + 1
    return -1


# Helper function for quickSearch()
def buildShiftTable(target, alphabet):
    shiftTable = {}
    for char in alphabet:
        shiftTable[char] = len(target) + 1
    for i in range(len(target)):
        character = target[i]
        shift = len(target) - i
        shiftTable[character] = shift
    return shiftTable


def quickSearch(searchString, target, alphabet):
    shiftTable = buildShiftTable(target, alphabet)
    searchIndex = 0
    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0
        while targetIndex < len(target) and target[targetIndex] == searchString[searchIndex+targetIndex]:
            targetIndex = targetIndex + 1
        if targetIndex == len(target):
            return searchIndex
        if searchIndex + len(target) < len(searchString):
            next = searchString[searchIndex + len(target)]
            shift = shiftTable[next]
            searchIndex = searchIndex + shift
        else:
            return -1
    return -1



# Helper function for kmpSearch()
def buildPrefixTable(target):
    #The first line of code just builds a list that has len(target)
    #items all of which are given the default value 0

    prefixTable = [0] * len(target)
    q = 0
    for p in range(1, len(target)):
        while q > 0 and target[q] != target[p]:
            q = prefixTable[q - 1]
        if target[q] == target[p]:
            q = q + 1
        prefixTable[p] = q
    return prefixTable



def kmpSearch(searchString, target):
    n = len(searchString)
    m = len(target)
    prefixTable = buildPrefixTable(target)
    q = 0
    for i in range(n):
        while q > 0 and target[q] != searchString[i]:
            q = prefixTable[q - 1]
        if target[q] == searchString[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return -1


#This line of code reads in a string of 30000 characters from file
def getBigString():
    with open ("searchData.txt", "r") as myfile:
        bigString = myfile.read()
    return bigString


theAlphabet = {'G', 'A', 'C', 'T'}

stringToSearch = getBigString()

target1 = 'CGTCCA'
target2 = 'TATATA'
target3 = 'CTCTATGTTTAAAGTTCGA'


#Time the functions

print('----------------------------------------------------')
print('kmpSearch() with target of ' + target1)
start = time.time()
print(kmpSearch(stringToSearch, target1))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('quickSearch() with target of ' + target1)
start = time.time()
print(quickSearch(stringToSearch, target1, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('basicStringSearch() with target of ' + target1)
start = time.time()
print(basicStringSearch(stringToSearch, target1))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('kmpSearch() with target of ' + target2)
start = time.time()
print(kmpSearch(stringToSearch, target2))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('quickSearch() with target of ' + target2)
start = time.time()
print(quickSearch(stringToSearch, target2, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('basicStringSearch() with target of ' + target2)
start = time.time()
print(basicStringSearch(stringToSearch, target2))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('kmpSearch() with target of ' + target3)
start = time.time()
print(kmpSearch(stringToSearch, target3))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('quickSearch() with target of ' + target3)
start = time.time()
print(quickSearch(stringToSearch, target3, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('basicStringSearch() with target of ' + target3)
start = time.time()
print(basicStringSearch(stringToSearch, target3))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')
