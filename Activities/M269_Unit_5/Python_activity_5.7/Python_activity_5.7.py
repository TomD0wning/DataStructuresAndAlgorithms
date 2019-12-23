#!/usr/bin/env python3

# Prim's algorithm for MST

# Authors: M269 module team
# Date: 18/08/13


from pythonds.graphs import PriorityQueue

# For the purposes of this activity, setting infinity to 100 is sufficient
infinity = 100

# graph6 corresponds to Figure 5.20 in Unit 5
graph6 = {
    'u': {'dist': infinity, 'edgeTo': {'v': 1, 'w': 2}},
    'v': {'dist': infinity, 'edgeTo': {'u': 1, 'x': 6, 'y': 5, 'z': 6}},
    'w': {'dist': infinity, 'edgeTo': {'u': 2, 'x': 2, 'z': 4}},
    'x': {'dist': infinity, 'edgeTo': {'v': 6, 'w': 2, 'y': 3}},
    'y': {'dist': infinity, 'edgeTo': {'x': 3, 'v': 5, 'z': 1}},
    'z': {'dist': infinity, 'edgeTo': {'v': 6, 'w': 4, 'y': 1}}}

# Example (formerly from Wikipedia) for testing purposes.
graph7 = {
    'A': {'dist': infinity, 'edgeTo': {'B': 7, 'D': 5}},
    'B': {'dist': infinity, 'edgeTo': {'A': 7, 'C': 8, 'D': 9, 'E': 7}},
    'C': {'dist': infinity, 'edgeTo': {'B': 8, 'E': 5}},
    'D': {'dist': infinity, 'edgeTo': {'A': 5, 'B': 9, 'E': 15, 'F': 6}},
    'E': {'dist': infinity, 'edgeTo': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9}},
    'F': {'dist': infinity, 'edgeTo': {'D': 6, 'E': 8, 'G': 11}},
    'G': {'dist': infinity, 'edgeTo': {'E': 9, 'F': 11}}}

# Example from
# http://www.cs.berkeley.edu/~vazirani/algorithms/chap5.pdf
# for testing purposes. Note our program finds a different
# tree of weight 14 from the one in the algorithms book!
# This is because it chooses C rather than B at step 2.
graph8 = {
    'A': {'dist': infinity, 'edgeTo': {'B': 5, 'C': 6, 'D': 4}},
    'B': {'dist': infinity, 'edgeTo': {'A': 5, 'C': 1, 'D': 2}},
    'C': {'dist': infinity, 'edgeTo': {'A': 6, 'B': 1, 'D': 2, 'E': 5, 'F': 3}},
    'D': {'dist': infinity, 'edgeTo': {'A': 4, 'B': 2, 'C': 2, 'F': 4}},
    'E': {'dist': infinity, 'edgeTo': {'C': 5, 'F': 4}},
    'F': {'dist': infinity, 'edgeTo': {'C': 3, 'D': 4, 'E': 4}}}


def prim(first, graph):
    pQueue = PriorityQueue()
    graph[first]['dist'] = 0
    for i in graph:
        pQueue.enqueue((graph[i]['dist'], i))
    mst = []
    # dictionary to record for each vertex in the queue its nearest vertex in the tree
    nearestInTreeTo = {}
    print('Removing front item', first, 'from priority queue')
    while not pQueue.isEmpty():
        u = pQueue.dequeue()

        print('Inspecting neighbours of vertex', u)

        for w in graph[u]['edgeTo']:

            edgeLen = graph[u]['edgeTo'][w]
            print(u, 'to', w,':', edgeLen)

            currentDist = graph[w]['dist']
            if w in pQueue and edgeLen < currentDist:
                graph[w]['dist'] = edgeLen
                pQueue.changePriority(w, edgeLen)
                nearestInTreeTo[w] = u

        if not pQueue.isEmpty():

            print('PriorityQueue is now :', pQueue.getEntries())
            print()

            nextVertex = pQueue.peek()
            print('Next vertex is:', nextVertex)
            weight = graph[nextVertex]['dist']
            newEdge = [[(nearestInTreeTo[nextVertex], nextVertex), weight]]


            print('Nearest in tree to', nextVertex,'is', nearestInTreeTo[nextVertex])
            print('Adding', newEdge, 'to the tree')
            mst = mst + [[(nearestInTreeTo[nextVertex], nextVertex), weight]]

            print('Tree is now :', mst)
            print()
            print('Removing front item', nextVertex, 'from priority queue')

    print('MST completed')
    return mst


def sumWeights(aTree):
    totalWeight = 0
    for edge in tree:
        totalWeight = totalWeight + edge[1]
    return totalWeight





print('***Calculating MST for graph6 starting at vertex u***')
print()
tree = prim('u', graph6)
print('Total weight of MST edges :', sumWeights(tree))
print('-------------------------------------------------')

print()
print('***Calculating MST for graph7 starting at vertex D***')
print()
tree = prim('D', graph7)
print('Total weight of MST edges :', sumWeights(tree))
print('-------------------------------------------------')

print()
print('***Calculating MST for graph8 starting at vertex A***')
print()
tree = prim('A', graph8)
print('Total weight of MST edges :', sumWeights(tree))
print('-------------------------------------------------')
