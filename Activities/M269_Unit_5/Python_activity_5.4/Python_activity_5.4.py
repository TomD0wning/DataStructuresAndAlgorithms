#!/usr/bin/env python3

# Program to implement and experiment with the BFS algorithm

# Authors: M269 Module Team
# Date: 7/8/13

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

graph3 = {
    1: {'colour': 'white', 'neighbours':[2, 3, 4]},
    2: {'colour': 'white', 'neighbours':[1, 3, 6]},
    3: {'colour': 'white', 'neighbours':[1, 5]},
    4: {'colour': 'white', 'neighbours':[1, 3]},
    5: {'colour': 'white', 'neighbours':[3]},
    6: {'colour': 'white', 'neighbours':[2, 7, 8]},
    7: {'colour': 'white', 'neighbours':[6]},
    8: {'colour': 'white', 'neighbours':[6, 9, 10]},
    9: {'colour': 'white', 'neighbours':[8]},
    10: {'colour': 'white', 'neighbours':[8]}}

def bfs(vertex, graph):
    g = graph
    queue = []
    queue.append(vertex)
    while len(queue) > 0:
        print('Queue is now', queue)
        print()
        u = queue.pop(0)
        print('Visiting', u, '- setting it to black')
        g[u]['colour'] = 'black'
        for w in g[u]['neighbours']:
            print('  checking neighbour', w, '- colour is', g[w]['colour'])
            if g[w]['colour'] is 'white':
                print('  appending neighbour', w, 'to queue and setting it to grey')
                queue.append(w)
                g[w]['colour'] = 'grey'



print('***BFS traversal for graph1 starting at 1***')
print()
bfs(1, graph1)
print('---------------------------------')
print()

print('***BFS traversal of graph2 starting at 0***')
print()
bfs(0, graph2)
print('---------------------------------')
print()

# Resetting graph1
graph1 = {
    1: {'colour': 'white', 'neighbours': [2, 3, 4]},
    2: {'colour': 'white', 'neighbours': [1, 4, 5]},
    3: {'colour': 'white', 'neighbours': [1, 4]},
    4: {'colour': 'white', 'neighbours': [1, 2, 3]},
    5: {'colour': 'white', 'neighbours': [2]}}

print('***BFS traversal of  graph1 again but starting at 3 this time***')
print()
bfs(3, graph1)
print('---------------------------------')
print()

print('***BFS traversal of graph3 starting at 1***')
print()
bfs(1, graph3)
print('---------------------------------')
