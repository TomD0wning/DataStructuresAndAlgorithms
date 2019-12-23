#!/usr/bin/env python3

# Authors: M269 Module Team
# Date: 20/11/12

def nameSearch(names, target):
    for eachName in names:
        if eachName == target:
            return True
    return False
        

def findHighest(intList):
    result = intList[0]
    for eachNum in intList:
        if eachNum > result:
            result = eachNum
    return result

def gradeStudents2(names, marks):
    result = []
    for i in range(len(names)):        
        result.append(names[i])
        if marks[i] >= 70 :
            result.append('A')
        elif marks[i] < 70 and marks[i] >= 50:
            result.append('B')
        elif marks[i] < 50 and marks[i] >= 30:
            result.append('C')
        else:
            result.append('F')
    return result


def gradeStudents(names, marks):
    result = []
    for i in range(len(names)):        
        result.append(names[i])
        if marks[i] >= 70:
            result.append('A')
        else:
            if marks[i] < 70 and marks[i] >= 50:
                result.append('B')
            else:
                if marks[i] < 50 and marks[i] >= 30:
                    result.append('C')
                else:
                    result.append('F')
    return result
 
 
 
numList = [5, 2, 21, 8, 20, 36, 1, 11, 13, 4, 17]
nameList = ['Smith', 'Jones', 'Turing', 'Bloggs', 'Meyer', 'Hampden']
markList = [30, 40, 50, 60, 70, 18]


print()
print('Testing nameSearch()')
print(nameSearch(nameList, 'Turing'))
print(nameSearch(nameList, 'Fred'))
print('______________________________')

print()
print('Testing findHighest()')
print(findHighest(numList))
print('______________________________')

print()
print('Testing gradeStudents()')
print(gradeStudents(nameList, markList))

