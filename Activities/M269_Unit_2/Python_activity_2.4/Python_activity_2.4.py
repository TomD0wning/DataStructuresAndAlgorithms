#!/usr/bin/env python3

def nameSearch(names, target):
    for name in names:
        if(name == target):
            return True
    return False

def findHighest(intList):
    highest = 0
    for number in intList:
        if(number > highest):
            highest = number
    return highest

def gradeStudents(names, marks):
    results = []
    count = 0
    for i in range(len(names)):
        results.append(names[i])
        if(marks[i] >= 70 ):
            results.append('A')
            continue
        elif(marks[i] < 70 and marks[i] >= 50 ):
            results.append('B')
        elif(marks[i] < 50 and marks[i] >= 30):
            results.append('C')
        else:
            results.append('F')
    return results

 
# Code to create lists to use with the fuctions 
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
