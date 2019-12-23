#!/usr/bin/env python3

# Author: M269 Module Team
# Date: 21/11/2012

def studentAverages(studentList, marksList):
    for i in range(len(studentList)):
        print(studentList[i], end = ' ')
        marks = marksList[i]
        total = 0
        for j in marks:
            total = total + j
        average = total / len(marks)
        print('has an average mark of:', average)
        if average > 84:
            print(studentList[i], 'is to be congratulated!')




  
 

# The following statement creates a list of student names

students = ['Smith', 'Jones', 'Turing', 'Bloggs', 'Meyer', 'Hampden']

# The following statement creates a list of lists. Each list in allMarks  
# represents the TMA marks for the corresponding student in students, such that  
# 'Smith' has the marks [56, 24, 68, 72], 'Jones' has the marks [24, 23, 18, 6], etc.

allMarks = [[56, 24, 68, 72], [24, 23, 18, 6], [99, 98, 89, 90], [15, 66, 27, 44], [76, 99, 87, 21], [14, 12, 55, 95]]

# The following statement calls the studentAverages() function with the two lists
# given above as the arguments. Observe the results of calling this function
# in the Command Output pane below.

studentAverages(students, allMarks)

