#!/usr/bin/env python3

# Program to implement and experiment with the DFS algorithm

# Authors: M269 Module Team
# Date: 6/8/13

graph1 = {
    1: {'colour': 'white', 'neighbours': [2, 3, 4]},
    2: {'colour': 'white', 'neighbours': [1, 4, 5]},
    3: {'colour': 'white', 'neighbours': [1, 4]},
    4: {'colour': 'white', 'neighbours': [1, 2, 3]},
    5: {'colour': 'white', 'neighbours': [2]}}

graph2 = {
    0: {'colour': 'white', 'neighbours': [1, 2, 3, 4]},
    1: {'colour': 'white', 'neighbours': [0, 3, 4]},
    2: {'colour': 'white', 'neighbours': [0, 5]},
    3: {'colour': 'white', 'neighbours': [0, 1, 5]},
    4: {'colour': 'white', 'neighbours': [0, 1]},
    5: {'colour': 'white', 'neighbours': [2, 3]}}



def dfs(vertex, graph):
    v = vertex
    g = graph

    print('Visiting', v, '- setting it to black')
    g[v]['colour'] = 'black'
    for w in g[v]['neighbours']:
        print('  checking neighbour', w, '- colour is', g[w]['colour'])
        if g[w]['colour'] is 'white':
            dfs(w, g)
            print('Unwinding back to', v)
    print('  all neighbours of', v, 'have been visited')


print('***DFS traversal of graph1 starting at 1***')
print()
dfs(1, graph1)

print('---------------------------------')
print()

print('***DFS traversal of graph2 starting at 0***')
print()
dfs(0, graph2)

print('---------------------------------')
print()

# Resetting graph1
graph1 = {
    1: {'colour': 'white', 'neighbours': [2, 3, 4]},
    2: {'colour': 'white', 'neighbours': [1, 4, 5]},
    3: {'colour': 'white', 'neighbours': [1, 4]},
    4: {'colour': 'white', 'neighbours': [1, 2, 3]},
    5: {'colour': 'white', 'neighbours': [2]}}

print('***Traversing graph1 again but starting at 3 this time***')
print()
dfs(3, graph1)
