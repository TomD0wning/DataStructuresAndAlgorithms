#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 11/12/13, 07/02/15


import time

# Helper function for quickSearch()
def buildShiftTable(target, alphabet):
    shiftTable = {}
    for character in alphabet:
        shiftTable[character] = len(target) + 1
    for i in range(len(target)):
        char = target[i]
        shift = len(target) - i
        shiftTable[char] = shift
    return shiftTable


def quickSearch(searchString, target, alphabet):
    print('-------------------------quickSearch()-------------------------')
    shiftTable = buildShiftTable(target, alphabet)
    searchIndex = 0
    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0
        while targetIndex < len(target) and target[targetIndex] == searchString[searchIndex+targetIndex]:
            targetIndex = targetIndex + 1
        if targetIndex == len(target):
            print(searchString)
            print(searchIndex * ' ' + target)
            return searchIndex
        if searchIndex + len(target) < len(searchString):
            next = searchString[searchIndex + len(target)]
            shift = shiftTable[next]
            searchIndex = searchIndex + shift
        else:
            print(searchString)
            print(searchIndex * ' ' + target)
            return -1
    return -1



def basicStringSearch(searchString, target):
    print('-------------------------basicStringSearch()-------------------------')
    searchIndex = 0
    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0
        while (targetIndex < len(target)) and target[targetIndex] == searchString[targetIndex + searchIndex]:
            targetIndex = targetIndex + 1
        if targetIndex == len(target):
            print(searchString)
            print(searchIndex * ' ' + target)
            return searchIndex
        searchIndex = searchIndex + 1
    print(searchString)
    print((searchIndex - 1) * ' ' + target)
    return -1


theAlphabet = {'G', 'A', 'C', 'T'}

stringToSearch = 'ATGAATACCCACCATGAATACCCACCATGAATACCCACCATGAATACCCACCATGAATACCCACCATGAATACCCACCATGAATACCCACCATGAATACCCACCATGAATACCCACCTTACAGAAACCTGGGAAAAGGCAATAAATATTATAAAAGGTGAACTTACAGAAGTAA'

target1 = 'CACC'
target2 = 'ACAG'
target3 = 'AAGTAA'
target4 = 'CCCC'

start = time.time()
print(quickSearch(stringToSearch, target1, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(basicStringSearch(stringToSearch, target1))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(quickSearch(stringToSearch, target2, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(basicStringSearch(stringToSearch, target2))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(quickSearch(stringToSearch, target3, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(basicStringSearch(stringToSearch, target3))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(quickSearch(stringToSearch, target4, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

start = time.time()
print(basicStringSearch(stringToSearch, target4))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')
