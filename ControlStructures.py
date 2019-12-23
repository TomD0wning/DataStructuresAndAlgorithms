#!/usr/bin/env python3

#Python control structures

x = int(input('Enter a number: '))

if x < 50:
    print('The number is less than 50')
else:
    print('The number is not less than 50')


aList = [1,2,'miss a few',99,100]

for n in aList:
    print(n)
    
for v in range(5):
    print(v)

for x in range(10,101):
    if x%2 ==0:
        print(x)

#Can also create a list that is more like a countdown
print(list(range(10,0,-1)))

#While statement

count = 10

while count > 0:
    print(count)
    count = count - 1
print('done')

#Task D
print('Task D','\n')

#1 input a string. If the string is ‘sesame’ print ‘open’, otherwise print ‘no entry!’
if input() == 'sesame':
    print('open','\n')
else:
    print('no entry','\n')

#2 Use range to print the squares of the numbers 1 to 9 in the format:
for a in range(1,10):
    print(a**2)

#3 Use a loop to print the odd numbers less than 20, by starting at 1 and looping round adding 2 each time as long as 20 has not been reached.

x = 1
while x < 20:
    if (x % 2) != 0: 
        print(x)
    x=x+2

#4 Form a string consisting of the first letters of the string ‘Richard Of York Gave Battle In Vain’ using the following algorithm.

#Split the string on the separator ' ' (i.e. a string consisting of a single space) and store the resulting list of words in a variable wordList.
#Create an empty string '' (i.e. a pair of quotes with nothing between them) and store it in a variable result.
#Iterate through wordList. For each word:
#Find the first letter and append it to result using the + operator.
#Print the result.

wordList = 'Richard Of York Gave Battle In Vain'.split(' ')
result = ''
for str in wordList:
    result += str[0]
print(result)