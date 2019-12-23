"""
Test file for M269 19J TMA01 Question 3

Student version 1: 16/4/19
"""

from TMA01_Q3 import is_sorted, is_palindrome

failed = 0
ran = 0


def test(name, function, argument, expected):
    """Report if test passed or failed."""
    global ran, failed

    original = argument.copy()
    actual = function(argument)
    if argument != original:
        print(name, 'FAILED: input changed from', original, 'to', argument)
        failed += 1
    elif actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1

# def test_sorted(name, argument, expected):
#     test(name, is_sorted, argument, expected)

def test_palindrome(name, argument, expected):
    test(name, is_palindrome, argument, expected)

# # Part (a)

# print('Tests for is_sorted')
# print('===================')
# test_sorted('sorted, no duplicate', [1,2,3,4], True)
# test_sorted('sorted, duplicate', [1,2,3,3,4], True)
# test_sorted('unsorted, no duplicate', [3,2,1], False)
# test_sorted('unsorted, duplicate', [3,2,2,1], False)
# test_sorted('single item', [1], True)
# print()

# Part (b)

print('Tests for is_palindrome')
print('=======================')
test_palindrome('palindrome, even items', ['a','n','n','a'], True)
test_palindrome('palindrome, odd items', ['a','n','a'], True)
test_palindrome('not palindrome, even items', ['a','n'], False)
test_palindrome('not palindrome, odd items', ['a','a','n'], False)
test_palindrome('single item', ['a'], True)
print()

print('Summary')
print('=======')
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''You passed all our tests. Well done! Now add YOUR tests.
Think of boundary values and other special cases for the inputs and output.''')
