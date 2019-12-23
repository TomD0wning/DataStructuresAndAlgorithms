#!/usr/bin/env python3

# Program to experiment with the BFS and DFS algorithms

# Authors: M269 Module Team
# Date: 13/8/13


tree1 = {
    0: {'colour': 'white', 'neighbours': [1, 2]},
    1: {'colour': 'white', 'neighbours': [0, 3, 4]},
    2: {'colour': 'white', 'neighbours': [0, 5, 6]},
    3: {'colour': 'white', 'neighbours': [1]},
    4: {'colour': 'white', 'neighbours': [1]},
    5: {'colour': 'white', 'neighbours': [2, 9]},
    6: {'colour': 'white', 'neighbours': [2, 7, 8]},
    7: {'colour': 'white', 'neighbours': [6]},
    8: {'colour': 'white', 'neighbours': [6, 10]},
    9: {'colour': 'white', 'neighbours': [5]},
    10: {'colour': 'white', 'neighbours': [8]}}



def bfs(vertex, graph):
    g = graph
    queue = []
    queue.append(vertex)

    while len(queue) > 0:
        u = queue.pop(0)
        g[u]['colour'] = 'black'
        print('Visiting', u)
        for w in g[u]['neighbours']:
            if g[w]['colour'] is 'white':
                queue.append(w)
                g[w]['colour'] = 'grey'


# This is the iterative version of dfs() as discussed in Python Activity 5.4
def dfs(vertex, graph):
    g = graph
    queue = []
    queue.append(vertex)
    while len(queue) > 0:
        u = queue.pop()
        print('Visiting', u)
        g[u]['colour'] = 'black'
        for w in g[u]['neighbours']:
            if g[w]['colour'] is 'white':
                queue.append(w)
                g[w]['colour'] = 'grey'




print('***BFS traversal of tree1 starting at 0***')
bfs(0, tree1)
print('---------------------------------')
print()

# Resetting tree1
tree1 = {
    0: {'colour': 'white', 'neighbours': [1, 2]},
    1: {'colour': 'white', 'neighbours': [0, 3, 4]},
    2: {'colour': 'white', 'neighbours': [0, 5, 6]},
    3: {'colour': 'white', 'neighbours': [1]},
    4: {'colour': 'white', 'neighbours': [1]},
    5: {'colour': 'white', 'neighbours': [2, 9]},
    6: {'colour': 'white', 'neighbours': [2, 7, 8]},
    7: {'colour': 'white', 'neighbours': [6]},
    8: {'colour': 'white', 'neighbours': [6, 10]},
    9: {'colour': 'white', 'neighbours': [5]},
    10: {'colour': 'white', 'neighbours': [8]}}

print('***DFS traversal of tree1 starting at 0***')
dfs(0, tree1)
print('---------------------------------')
print()
