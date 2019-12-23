#! /usr/bin/env python3


#Basic IO in python

name = input('Enter your name: ')
print('You entered',name,sep=' ',end='\n')

#input is treated as a string, therefore to use an int or float, it needs to be cast to the appropriate.

x = input('Enter a whole number: ')
print(int(x) +10)

#casting can be done the opposite way too

y = 'Result is ' + str(100)
print(y)


print('task 1.9',end='\n')

#Divide 22 by 7 using the / operator and display the result to 10 decimal places.

print(round((22/7),10))

#The variables aName, anAge and aYear hold the values 'Alan', 100 and 2012 respectively. Use these variables to display the following
#Alan was 100 years old in 2012

aName='Alan'
anAge=100
aYear=2012

print(aName,'was',int(anAge),'years old in', int(aYear))

# Input a string, convert it to an integer, store it in a suitable variable, and then print the number and its square, in the format of the example below.
# Your number is 12
# Its square is 144

inputNumber = int(input('Enter a number: '))

print('Your number is ', str(inputNumber))
print('Its square is: ', str(inputNumber**2))
















