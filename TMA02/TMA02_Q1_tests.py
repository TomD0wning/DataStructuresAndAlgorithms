"""
Test file for M269 19J TMA02 Q1
Student version 1: 6/6/19
"""

from TMA02_Q1 import selectionMedian

failed = 0
ran = 0

def test(name, numbers, expected):
    """Test the selectionMedian function and report if it failed or passed."""
    global ran, failed

    actual = selectionMedian(numbers)
    ran += 1
    if actual != expected:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    else:
        print(name, 'OK')

# The following tests check the function you changed.

print('Tests for selectionMedian')
print('=========================')
test('3 numbers, unsorted', [77, 111, 55], 77)
test('3 numbers, sorted', [55, 77, 111], 77)
test('9 numbers, unsorted', [2, 9, 4, 3, 1, 17, 29, 5, 1], 4)
print()

print('Summary')
print('=======')
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''You passed all our tests. Well done! Now add YOUR tests.
Remember the input is assumed to have an odd length.
Think of boundary values and other special cases for the inputs and output.''')