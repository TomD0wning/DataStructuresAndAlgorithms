#!/usr/bin/env python3

print("Not hello world again")
if 1+1 == 2:
    print("hhmmm")

print("some variables and math")

a=2
b=6
c=a+b
print(c)

print("How many seconds are there in a leap year?")
print((60*60*24)*366)

print("What is the mean of 5, 12 and 13?")
print((5+12+13)/3,'\n')

print("What is the remainder when 99999199999 is divided by 919?")
print("Whole number", 99999199999//919)
print("Remainder", 99999199999%919,'\n')

print("Is it true or false that 17711 multiplied by 6765 is greater than 10946 multiplied by itself?")
if (17711 * 6765) > 10946**2:
    print("True",'\n')
else:
    print("False",'\n')


print("How many ways can you find to make exactly 100 by using the numbers 1 to 9 once each and the operations of addition and multiplication?")
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8*9)
print(1*2*3 + 4 + 5 + 6 + 7 + 8*9)
print(1*2*3*4 + 5 + 6 + 7*8 + 9)


#Creating a list. A list in python can contain any data type
print("Some list operations",'\n')

myList = [12,'tea',42.0]
print(myList)

#Len is a function as it takes an arguement
print("List length: ", len(myList))

print("Element 1: ", myList[1])

#Append is a method as it operated on an object & uses dot notation
myList.append('coffee')

print(myList)

myList[0] = 100

result = myList.pop(1)
print("popped record is:",result)

print(myList)

#Some string operations, note that strings are immutable in python
print("String Operations")

print("Create a list aList containing the items 'age', 'before' and 'beauty'. Change the first item to 'pride comes'. Remove the last item. Finally, append the item 'a fall'")
aList = ['age','before','beauty']
print(aList)
aList[0]='pride comes'
aList.pop()
aList.append('a fall')
print(aList,'\n')


print("Create a list list1 containing the items 1, 2, 3, 5, and 8 and another list2 containing the items 13 and 21. Create a third list list3 which joins these two together.")

list1 = list(range(0,6))
list1.append(8)

list2 = [13,21]

list3  = list1+list2
print(list3)

print(list3[1:6])

print("Create a string 'tarama' and another 'salata'. Append the second string to the first.")

t = "tarama"
s = "salata"
ts = t+s

print("In the combined string, find the first index at which 'ta' appears. Count the occurrences of the character 'a'.")
print(ts.index('ta'))
print(ts.count('a'))

print("Finally, split the string on the separator 'a'.")
print(ts.split('a'))



#Tuples and sets. Again as with strings Tuples are immutable. sets are defined using curly braces

aSet = {1,'red'}

aSet.add('blue')

print(aSet)

#duplicates are not allowed in a set, therefore the below code does nothing

aSet.add('blue')

aSet.remove('red')

len(aSet)

#Strings can be transformed into a set, but will only keep unique values

set('cocoa')

# | or union can be used to join two sets together

bSet = {'m','v','d','e'}
cSet = {'m','e'}

print("using pipe: ",bSet | cSet)
print("using union method",bSet.union(cSet),'\n')

#  & or intersect produce a new set containing common items to both sets

print("using ampersand ", bSet & cSet)
print("using intersect", bSet.intersection(cSet),'\n')

#check if an item is in a set
dSet = {'a','b','c'}
print("is a in dSet? ", 'a' in dSet)
print("is z in dSet? ", 'z' in dSet)










