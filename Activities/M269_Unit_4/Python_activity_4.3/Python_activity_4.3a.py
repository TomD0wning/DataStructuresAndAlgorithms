#!/usr/bin/env python3


#Authors: M269 Module Team
#Date: 11/12/13, 07/02/15

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


def quickSearch (searchString, target, alphabet):
    print('-------------------------quickSearch()-------------------------')
    shiftTable = buildShiftTable(target, alphabet)
    print('shiftTable =' + str(shiftTable))
    print()
    searchIndex = 0
    print(searchString)
    print(target)
    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0
        while targetIndex < len(target) and target[targetIndex] == searchString[searchIndex + targetIndex]:
            targetIndex = targetIndex + 1
        if targetIndex == len(target):
            print('Found')
            return searchIndex
        if searchIndex + len(target) < len(searchString):
            next = searchString[searchIndex + len(target)]
            shift = shiftTable[next]
            print('Failed comparison, next character in searchString is '  + searchString[searchIndex + len(target)] + ', so slide target along by ' + str(shift))
            print()
            searchIndex = searchIndex + shift
            print(searchString)
            print(searchIndex * ' ' + target)
        else:
            print('Not found')
            return -1
    return -1




theAlphabet = {'G', 'A', 'C', 'T'}

stringToSearch = 'ATGAATACCCACCTTACAGAAACCTGGGAAAAGGCAATAAATATTATAAAAGGTGAACTTACAGAAGTAA'

target1 = 'ACAG'
target2 = 'AAGTAA'
target3 = 'CCCC'

print(quickSearch(stringToSearch, target1, theAlphabet))
print()
print(quickSearch(stringToSearch, target2, theAlphabet))
print()
print(quickSearch(stringToSearch, target3, theAlphabet))
