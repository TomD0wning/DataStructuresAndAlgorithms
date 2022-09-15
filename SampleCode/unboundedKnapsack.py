#!/usr/bin/env python3
def knapsack(itemWeights, itemValues, bagWeightLimit):
    bagValues = [0] * (bagWeightLimit + 1)

    for w in range(1, bagWeightLimit + 1):
        bestValue = 0
        for x in range(len(itemWeights)):
            if itemWeights[x] <= w:
                previousBagWeight = w - itemWeights[x]
                possibleBest = bagValues[previousBagWeight] + itemValues[x]
                if possibleBest > bestValue:
                    bestValue = possibleBest
        bagValues[w] = bestValue

    print(bagValues[w])


itemWeights = [12, 2, 1, 4, 1]
itemValues = [4, 2, 1, 10, 2]
bagWeightLimit = 15

knapsack(itemWeights, itemValues, bagWeightLimit)
