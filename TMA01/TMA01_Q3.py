"""
Code file for M269 19J TMA01 Question 3

Student version 1: 7/3/19
"""

# Part (a)

def is_sorted(numbers):
    return all(numbers[x] <= numbers[x+1] for x in range(len(numbers)-1))

# Part (b)

def is_palindrome(the_list):
    listLength = len(the_list)
    for character in the_list:
        if character != the_list[listLength -1]:
            return False
        else:
            listLength-=1
            continue
    return True