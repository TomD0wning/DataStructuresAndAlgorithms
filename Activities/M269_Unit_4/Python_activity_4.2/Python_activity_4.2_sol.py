#!/usr/bin/env python3

#Authors: M269 Module Team
#Date: 09/12/13




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


# Alternative version that uses an outer for loop rather than a while loop
def basicStringSearch2(searchString, target):
    searchIndex = 0
    for i in range(len(searchString) - len(target) + 1):
        targetIndex = 0
        while (targetIndex < len(target)) and target[targetIndex] == searchString[targetIndex + searchIndex]:
            targetIndex = targetIndex + 1
        if targetIndex == len(target):
            return searchIndex
        searchIndex = searchIndex + 1
    return -1





print(basicStringSearch('per ardua ad alta', 'per'))
print(basicStringSearch('per ardua ad alta', 'lta'))
print(basicStringSearch('per ardua ad alta', 'ad'))
print(basicStringSearch('per ardua ad alta', 'astra'))
