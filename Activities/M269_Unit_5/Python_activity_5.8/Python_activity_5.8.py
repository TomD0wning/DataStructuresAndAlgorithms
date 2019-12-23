#!/usr/bin/env python3

# Topsort algorithm


# Authors: M269 Module Team
# Date: 14/8/13

# digraph1 corresponds to Figure 5.27 in Unit 5
digraph1 = {
    1: [2],
    2: [],
    3: [1, 6],
    4: [3, 5],
    5: [],
    6: [2, 5]}

# digraph2 corresponds to Figure 7.18 in Miller & Ranum
digraph2 = {
    '3/4 cup milk':['1 cup mix'],
    '1 egg':['1 cup mix'],
    '1 Tbl Oil':['1 cup mix'],
    '1 cup mix':['pour 1/4 cup', 'heat syrup'],
    'heat syrup':['eat'],
    'heat griddle':['pour 1/4 cup'],
    'pour 1/4 cup':['turn when bubbly'],
    'turn when bubbly':['eat'],
    'eat':[]
}

# Returns a dictionary of incoming edges at each vertex
def getVertexDictionary(aDigraph):
    vDict = {}
    for v in aDigraph:
        vDict[v] = 0
    for v in aDigraph:
        for w in aDigraph[v]:
            vDict[w] = vDict[w] + 1
    return vDict

# Returns the set of vertices with no incoming edges
def getVertexSet(aDict):
    vertexSet = set()
    for v in aDict:
        if aDict[v] == 0:
            vertexSet.add(v)
    return vertexSet

# Finds topological sort
def topSort(digraph):
    # Initial count of incoming edges at each vertex
    vertexDict = getVertexDictionary(digraph)
    print('Initial dictionary of incoming edges at each vertex:', vertexDict)
    print()
    # Holding set of vertices with zero incoming edges
    vertexSet = getVertexSet(vertexDict)
    # List to hold vertices in topologically sorted order
    topsort = []

    while len(vertexSet) > 0:
        print('   Set of vertices with no incoming edges:', vertexSet)
        # Remove a vertex with no incoming edges from the holding set...
        v = vertexSet.pop()

        # ...and from the count
        del vertexDict[v]
        print('  ', v, 'removed from set and dictionary')
        # ...and add the vertex to topological sort
        topsort.append(v)
        # For each vertex that the removed vertex has an edge to
        for w in digraph[v]:
            print('      Decreasing incoming edges count for', w)
            # Decrease the incoming vertex count...
            vertexDict[w] = vertexDict[w] - 1
            # ... and if its count becomes zero add the vertex to the holding set
            if vertexDict[w] == 0:
                vertexSet.add(w)
                print('     ', w, 'now has zero incoming edges so added to the set')
        print('   Dictionary is now:', vertexDict)
        print()
    return topsort




print('***Topological sort of digraph1***')
print()
print('Result for digraph1 is', topSort(digraph1))

print('---------------------------------')
print()
print('***Topological sort of digraph2***')
print()
print('Result for digraph2 is', topSort(digraph2))
