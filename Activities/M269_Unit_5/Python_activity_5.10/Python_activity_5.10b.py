#!/usr/bin/env python3

# Dynamic programming example for unbounded knapsack problem that keeps track of items added

# Authors: M269 Module Team
# Date: 28/8/13

def knapsack(itemWeights, itemValues, itemNames, bagWeightLimit):

    # Set up a list that will hold optimum values for weights 1 to bagWeightLimit.
    bagValues = [0] * (bagWeightLimit + 1)

    # Set up a list that will hold the previous weight of a bag before another jewel is added
    previousBagWeights = [None] * (bagWeightLimit + 1)

    # Set up a list to hold items that could be added for weights 1 to bagWeightLimit.
    itemAtBagWeight =[None] * (bagWeightLimit + 1)

    # Each of the above lists are given a dummy value at index zero for convenience
    # (which we won't use) as we want to index the lists from 1 rather than zero.

    for w in range(1, bagWeightLimit + 1):

        bestValueForWeight = 0
        previousBagWeight = None
        selectedItem = None

        for i in range(len(itemWeights)):
            if itemWeights[i] <= w:
                possiblePrevWeight = w - itemWeights[i]
                possibleBestValue = bagValues[possiblePrevWeight] + itemValues[i]
                if possibleBestValue > bestValueForWeight:
                    bestValueForWeight = possibleBestValue
                    previousBagWeight = possiblePrevWeight
                    selectedItem = itemNames[i]
        bagValues[w] = bestValueForWeight
        previousBagWeights[w] = previousBagWeight
        itemAtBagWeight[w] = selectedItem

    print('-----------------------------------------------------------------')
    print('The optimum total value for a bag with a weight limit of', w, 'is', bagValues[w])
    bag = []
    j = bagWeightLimit
    while j > 0:
        itemToAdd = itemAtBagWeight[j]
        bag.append(itemToAdd)
        j = previousBagWeights[j]
    print('With the items', bag[::-1])
    print('-----------------------------------------------------------------')


# Code to test the function. Weights and values from an example on Wikipedia.
knapsack([12, 2, 1, 4, 1], [4, 2, 1, 10, 2], ['green', 'blue', 'red', 'yellow', 'grey'], 15)
