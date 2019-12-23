#!/usr/bin/env python3

# Contains the function tsp() which along with the helper function
# getTourLength() implements a brute-force solution to the TSP problem.

# Authors: M269 Module Team
# Date: 30/08/13

import itertools

# Dictionary representing the graph of cities

cities = {
     'Scunthorpe': {'routeTo':{'Bridlington': 31, 'Wick': 514, 'Bognor': 252, 'Nuneaton': 111,
                                       'Luton': 117, 'Wrexham': 142, 'Penzance': 318,}},
     'Bridlington':{'routeTo':{'Scunthorpe': 31, 'Luton': 142, 'Nuneaton': 115,
                                       'Bognor': 209, 'Penzance': 426, 'Wrexham': 162, 'Wick': 512}},
     'Luton':{'routeTo':{'Bridlington': 142, 'Scunthorpe': 117, 'Wick': 627,
                                 'Bognor': 112, 'Wrexham': 151, 'Nuneaton': 65, 'Penzance': 320}},
     'Nuneaton':{'routeTo':{'Luton': 65, 'Wick': 566, 'Bridlington': 115,
                                    'Scunthorpe': 111, 'Bognor': 161, 'Wrexham': 90, 'Penzance': 219}},
     'Bognor':{'routeTo':{'Scunthorpe': 252, 'Wick': 720, 'Bridlington': 209,
                                  'Luton': 112, 'Nuneaton': 161, 'Wrexham': 243, 'Penzance': 258}},
     'Penzance':{'routeTo':{'Wick': 809, 'Scunthorpe': 318, 'Bridlington': 426,
                                    'Luton': 320, 'Nuneaton': 219, 'Wrexham': 333, 'Bognor': 258}},
     'Wick':{'routeTo':{'Penzance': 809, 'Scunthorpe': 514, 'Bridlington': 512,
                                'Luton': 627, 'Wrexham': 508, 'Nuneaton': 566, 'Bognor': 720}},
     'Wrexham':{'routeTo':{'Penzance': 333, 'Scunthorpe': 142, 'Bridlington': 162,
                                   'Luton': 151, 'Nuneaton': 90, 'Wick': 508, 'Bognor': 243}}
         }

def tsp(startPoint):
    allCities = list(cities[startPoint]['routeTo'])
    bestTour = ''
    bestTourLength = 99999999999999
    worstTour = ''
    worstTourLength = 0
    for i in itertools.permutations(allCities):
        tourLength = getTourLength(startPoint, i)
        if tourLength < bestTourLength:
            bestTour = i
            bestTourLength = tourLength
        elif tourLength > worstTourLength:
            worstTour = i
            worstTourLength = tourLength
    print('Shortest tour starting and ending in', startPoint, 'is:', bestTour, 'length', bestTourLength)
    print('Longest tour starting and ending in', startPoint, 'is:', worstTour, 'length', worstTourLength)


def getTourLength(startPoint, tour):
    tourLength = cities[startPoint] ['routeTo'] [tour[0]]
    lastVisited = tour[len(tour) - 1]
    for j in range(len(tour) - 1):
        if tour[j] != tour[j + 1]:
            theEdge = cities[tour[j]] ['routeTo'] [tour[j + 1]]
            tourLength = tourLength + theEdge
    tourLength = tourLength + cities[lastVisited] ['routeTo'] [startPoint]
    return tourLength


tsp('Scunthorpe')
