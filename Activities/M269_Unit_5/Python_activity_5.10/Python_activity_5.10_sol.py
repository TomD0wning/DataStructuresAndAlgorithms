#!/usr/bin/env python3

# Dynamic programming example for unbounded knapsack problem

# Authors: M269 Module Team
# Date: 28/8/13


def knapsack(itemWeights, itemValues, bagWeightLimit):

    # Set up a list that will hold optimum values for weights 1 to bagWeightLimit.
    # We give index zero a dummy value for convenience (which we won't use) as we
    # want to index bagValues from 1 rather than zero.
    bagValues = [0] * (bagWeightLimit + 1)

    for w in range(1, bagWeightLimit + 1):
        bestValueForWeight = 0
        for i in range(len(itemWeights)):
            if itemWeights[i] <= w:
                previousBagWeight = w - itemWeights[i]
                possibleBestValue = bagValues[previousBagWeight] + itemValues[i]
                if possibleBestValue > bestValueForWeight:
                    bestValueForWeight = possibleBestValue
        bagValues[w] = bestValueForWeight

    print('-----------------------------------------------------------------')
    print('Given a list of item weights', itemWeights, 'and a')
    print('parallel list of item values', itemValues)
    print()
    print('The optimum total value for a bag with a weight limit of', w, 'is', bagValues[bagWeightLimit])
    print('-----------------------------------------------------------------')


# Code to test the function

# Experiment by changing the values of itemWeights, itemValues
# and bagWeightLimit to your own values. The only proviso is that
# itemWeights and itemValues must have the same number of items.

itemWeights = [12, 2, 1, 4, 1]
itemValues = [4, 2, 1, 10, 2]
bagWeightLimit = 15

knapsack(itemWeights, itemValues, bagWeightLimit)
