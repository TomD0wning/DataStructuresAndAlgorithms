"""
Test file for M269 19J TMA02 Q3
Student version 1: 1/07/19
"""

# deepcopy() is needed to fully copy a graph, incl. its adjacency sets
# this will allow us to test your code doesn't change the input graph
from copy import deepcopy

from TMA02_Q3_graph import Graph
from TMA02_Q3 import common, suggested_friends

failed = 0
ran = 0

def test_common(name, graph, person1, person2, expected):
    """Test the common() function and report if it failed or passed."""
    global ran, failed

    original = deepcopy(graph)
    actual = common(graph, person1, person2)
    ran += 1
    if actual != expected:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    elif graph != original:
        print(name, 'FAILED: graph was changed')
        failed += 1
    else:
        print(name, 'OK')

def test_suggested(name, graph, person, expected):
    """Test the suggested_friends() function and report the result."""
    global ran, failed

    original = deepcopy(graph)
    actual = suggested_friends(graph, person)
    ran += 1
    if actual not in expected:
        print(name, 'FAILED: got', actual, 'instead of one of', expected)
        failed += 1
    elif graph != original:
        print(name, 'FAILED: graph was changed')
        failed += 1
    else:
        print(name, 'OK')

# The following graph is given in the question.

example = Graph()
example.add_edge('Xian', 'Bob')
example.add_edge('Bob', 'Alice')
example.add_edge('Bob', 'Yasmin')
example.add_edge('Alice', 'Cleo')
example.add_edge('Yasmin', 'Cleo')
example.add_edge('Cleo', 'Zoe')
example.add_edge('Fran', 'George')
example.add_edge('George', 'Halim')

# The following tests check the Graph code we provide.
# The tests are written as assertions to not clutter your screen with messages.

assert len(example.nodes()) == 9
assert len(example.edges()) == 8
assert example.has_edge('Alice', 'Bob') and not example.has_edge('Al', 'Bob')
assert example.neighbours('Bob') == {'Xian', 'Yasmin', 'Alice'}
assert example.neighbours('Fran') == {'George'}

assert example.bfs('Halim') == example.dfs('Halim') == ['Halim', 'George', 'Fran']
assert example.bfs('Xian') in [ # possible BFS paths:
    ['Xian', 'Bob', 'Alice', 'Yasmin', 'Cleo', 'Zoe'],
    ['Xian', 'Bob', 'Yasmin', 'Alice', 'Cleo', 'Zoe']
]
assert example.dfs('Xian') in [ # possible DFS paths:
    ['Xian', 'Bob', 'Alice', 'Cleo', 'Yasmin', 'Zoe'],
    ['Xian', 'Bob', 'Alice', 'Cleo', 'Zoe', 'Yasmin'],
    ['Xian', 'Bob', 'Yasmin', 'Cleo', 'Alice', 'Zoe'],
    ['Xian', 'Bob', 'Yasmin', 'Cleo', 'Zoe', 'Alice']
]

# The following tests check the function you changed.

print('Tests for common')
print('================')
test_common('Xian and Cleo', example, 'Xian', 'Cleo', 0)
test_common('Xian and Alice', example, 'Xian', 'Alice', 1)
test_common('Alice and Yasmin', example, 'Alice', 'Yasmin', 2)
test_common('Zoe and Fran', example, 'Zoe', 'Fran', 0)
print()

# The following should still work after you changed the function

print('Tests for suggested_friends')
print('===========================')
test_suggested('for George', example, 'George', [[]])
test_suggested('for Halim', example, 'Halim', [['Fran']])
test_suggested('for Alice', example, 'Alice',
    [['Yasmin', 'Zoe', 'Xian'], ['Yasmin', 'Xian', 'Zoe']])
print()

print('Summary')
print('=======')
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''You passed all our tests. Well done! Now add YOUR tests.
Think of boundary values and other special cases for the inputs and output.''')
