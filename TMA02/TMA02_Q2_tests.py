"""
Test file for M269 19J TMA02 Question 2

Student version 1: 6/6/19
"""

from TMA02_Q2_BST import BST, TreeNode
from TMA02_Q2 import Bibliography

failed = 0
ran = 0

def test_reference(name, bibliography, key, expected):
    """Test the getReference() method and report if it failed or passed."""
    global ran, failed

    actual = bibliography.getReference(key)
    ran += 1
    if actual != expected:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    else:
        print(name, 'OK')

def test_bibliography(name, bibliography, expected):
    """Test the outputBibliography() method and report if it failed or passed."""
    global ran, failed

    actual = bibliography.outputBibliography()
    ran += 1
    if actual != expected:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    else:
        print(name, 'OK')

# Keys and values to be tested
millerkey = 'Miller, B. N., Ranum, D. L. (2011)'
millervalue = 'Problem Solving with Algorithms and Data Structures using Python, \
2nd edn, Oregon, Franklin, Beedle & Associates, Incorporated.'

ou2013key = 'The Open University (2013)'
ou2013value1 = 'Logic and the limits of computing, Milton Keynes, The Open University'
ou2013value2 = 'Another fascinating booklet, Milton Keynes, The Open University'

adamskey = 'Adams, A (1999)'
adamsvalue = 'A grand read'

patelkey = 'Patel, I (2007)'
patelvalue = 'My story'


myBib = Bibliography()

test_reference('empty bib', myBib, millerkey, None)

myBib.addReference(millerkey, millervalue)
myBib.addReference(ou2013key, ou2013value1)

test_reference('M&R added', myBib, millerkey, millervalue)
test_reference('Logic added', myBib, ou2013key, ou2013value1)

myBib.removeReference(ou2013key)

test_reference('Logic removed', myBib, ou2013key, None)
test_reference('M&R still there', myBib, millerkey, millervalue)

myBib.addReference(ou2013key, ou2013value2)

test_reference('booklet added', myBib, ou2013key, ou2013value2)

myBib.addReference(adamskey, adamsvalue)
myBib.addReference(patelkey, patelvalue)

test_bibliography('listing', myBib,
    adamskey + ' ' + adamsvalue + '\n\n'
    + millerkey + ' '  + millervalue + '\n\n'
    + patelkey + ' ' + patelvalue + '\n\n'
    + ou2013key + ' ' + ou2013value2 + '\n\n')

print()
print('Summary')
Bibliography.outputBibliography(myBib)
print('=======')
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''You passed all our tests. Well done! Now add YOUR tests.
Think of boundary values and other special cases for the inputs and output.''')
