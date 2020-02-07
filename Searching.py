#!/usr/bin/env python3

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

# Like quick sort, quick select is a recursive divide-and-conquer algorithm that stops when the base case is reached: the partition examined has only one item. Unlike quick sort, it only recurses into the partition that holds the item that is being searched for. Quick select has average complexity O(n); a naïve selection algorithm using quick sort would have at least complexity O(n log n)

def quickSelect(k, aList):

    if len(aList) == 1:
        return aList[0]

    pivotValue = aList[0]
    leftPart = []
    rightPart = []

    for item in aList[1:]:
        if item < pivotValue:
             leftPart.append(item)
        else:
            rightPart.append(item)

    if len(leftPart) >= k:
        return quickSelect(k, leftPart)
    elif len(leftPart) == k - 1:
        return pivotValue
    else:
        return quickSelect(k - len(leftPart) -1, rightPart)

theList = [9, 32, 16, 23, 9, 26, 8, 20, 18, 3]
print(quickSelect(7, theList))


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
    shiftTable = buildShiftTable(target, alphabet)
    searchIndex = 0

    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0
        while targetIndex < len(target) and target[targetIndex] == searchString[searchIndex + targetIndex]:
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

def buildPrefixTable(target):
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

def chopIntoPairs(aNumber):
    numString = str(aNumber)
    pairs = []
    for i in range( 0,len(numString), 2):
        pairs.append(int(numString[i: i + 2]))
    return pairs

def hashFold(num, tableSize):
    sum = 0
    splitNum = chopIntoPairs(num)
    for p in range(len(splitNum)):
        sum = sum + splitNum[p]

    return sum%tableSize


print(hashFold(123456,80))
print(hashFold(431941,80))
print(hashFold(789012,80))
print(hashFold(60375,80))