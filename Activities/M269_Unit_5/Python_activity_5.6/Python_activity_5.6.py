#!/usr/bin/env python3

# Implementation Dijkstra's algorithm

# M269 module team
# version 1.0 15/08/13

from pythonds.graphs import PriorityQueue

# For the purposes of this activity, setting infinity to 100 is sufficient
infinity = 100

# graph4 corresponds to Figure 5.20 in Unit 5
graph4 = {
    'u': {'dist': infinity, 'edgeTo': {'v': 1, 'w': 2}},
    'v': {'dist': infinity, 'edgeTo': {'u': 1, 'x': 6, 'y': 5, 'z': 6}},
    'w': {'dist': infinity, 'edgeTo': {'u': 2, 'x': 2, 'z': 4}},
    'x': {'dist': infinity, 'edgeTo': {'v': 6, 'w': 2, 'y': 3}},
    'y': {'dist': infinity, 'edgeTo': {'x': 3, 'v': 5, 'z': 1}},
    'z': {'dist': infinity, 'edgeTo': {'v': 6, 'w': 4, 'y': 1}}}


# graph5 corresponds to Figure 7.29 in Miller and Ranum
graph5 = {
    'u': {'dist': infinity, 'edgeTo': {'v': 2, 'w': 5, 'x': 1}},
    'v': {'dist': infinity, 'edgeTo': {'u': 2, 'w': 3, 'x': 2}},
    'w': {'dist': infinity, 'edgeTo': {'u': 5, 'v': 3, 'x': 3, 'y': 1, 'z': 5}},
    'x': {'dist': infinity, 'edgeTo': {'u': 1, 'v': 2, 'w': 3, 'y': 1}},
    'y': {'dist': infinity, 'edgeTo': {'x': 1, 'w': 1, 'z': 1}},
    'z': {'dist': infinity, 'edgeTo': {'w': 5, 'y': 1}}}


def dijkstra(source, graph):
    pQueue = PriorityQueue()
    graph[source]['dist'] = 0
    for v in graph:
        pQueue.enqueue((graph[v]['dist'], v))
    while not pQueue.isEmpty():
        u = pQueue.dequeue()
        baseDist = graph[u]['dist']
        print('Visiting',u, 'at distance', baseDist)
        print('Edges from this vertex', graph[u]['edgeTo'])
        for w in graph[u]['edgeTo']:
            edgeLen = graph[u]['edgeTo'][w]
            newDist = baseDist + edgeLen
            currentDist = graph[w]['dist']
            if newDist < currentDist:
                graph[w]['dist'] = newDist
                print('Distance to', w, 'set to', baseDist, '+', edgeLen, '=', newDist)
                pQueue.changePriority(w, newDist)
        print()
    # Print the results
    print('Final result: distances of all vertices from ' + source)
    distancesList = []
    for v in graph:
        distancesList.append((v, graph[v]['dist']))
    print(distancesList)



# Code to test dijkstra()

source = 'u'
dijkstra(source, graph4)
