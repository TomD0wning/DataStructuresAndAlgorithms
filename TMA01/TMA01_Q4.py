"""
Code file for M269 19J TMA01 Question 4

Student version 1: 1/5/19
"""

from TMA01_Q4_stack import Stack

# Part (d)

def reverse_to_list(s):
    reversed_list = []
    x = s.size();
    while x != 0:
        reversed_list.append(s.items[x -1])
        x -=1
    return reversed_list

# Part (e)

def is_palindrome(the_list):
    s = Stack()

    for x in the_list:
        s.push(x)
    for n in the_list:
        if n == s.peek():
            s.pop()
        else:
            continue
    return s.isEmpty()