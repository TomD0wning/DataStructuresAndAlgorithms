#!/usr/bin/env python3

a = [1,2,3,4,5]
b = ['a', 'b', 'c', 'd', 'e', 'f']

x = a[:3]
print('x references: ', x)

y = b[4:]
print('y references:', y)

z = a[3]/a[2]
print('z references: ', z)


# The following function should go through all the numbers in the argument list, add together all the positive numbers there, and 
# return that total. The function should return zero if there are no positive numbers in the list
# def add_positive(integers):
#     while number from integers
#         if number != -1
#             total + 1
#     return total


def add_positive(integers):
    total = 0
    for x in integers:
        if x > 0:
            total+=x

    if total > 0:
        return total
    else:
        return 0


print(add_positive([3, 2, 1, 0, -1]))