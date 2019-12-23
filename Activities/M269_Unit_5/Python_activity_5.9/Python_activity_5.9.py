#!/usr/bin/env python3

# Dynamic programming example for knapsack problem - Treasure Island scenario

# Authors: M269 Module Team
# Date: 14/8/13


bagWeightLimit = 12
jewelWeights = [2, 4, 5]
jewelValues = [3, 6, 7]
jewelNames = ['ruby', 'sapphire', 'diamond']

# Set up a list that will hold optimum values for weights 1 to bagWeightLimit.
# We give index zero a dummy value for convenience (which we won't use) as we
# want to index bagValues from 1 rather than zero.
bagValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for w in range(1, bagWeightLimit + 1):
    print('Weight limit of bag =', w)
    bestValueForWeight = 0
    for jewel in range(3):
        print('Checking if a', jewelNames[jewel], 'weight =', jewelWeights[jewel], ', value =', jewelValues[jewel], 'could be added')
        if jewelWeights[jewel] <= w:
            print('  A', jewelNames[jewel], 'could be added')
            previousBagWeight = w - jewelWeights[jewel]
            print('  Without the', jewelNames[jewel],'the previous weight of the bag must have been', w, '-', jewelWeights[jewel], '=', previousBagWeight)
            print('  The best possible value for a bag with a weight limit of', previousBagWeight, 'was', bagValues[previousBagWeight])
            possibleBestValue = bagValues[previousBagWeight] + jewelValues[jewel]
            print('  Adding the value of a', jewelNames[jewel], 'gives a total value for this bag of', bagValues[previousBagWeight], '+', jewelValues[jewel], '=', possibleBestValue)
            if possibleBestValue > bestValueForWeight:
                bestValueForWeight = possibleBestValue
                print(' ', possibleBestValue, 'is a new best value for a bag of weight', w)
            else:
                print('  This is not better than the current best value of', bestValueForWeight)
        else:
            print('  A', jewelNames[jewel], 'would exceed the bag weight limit')

    bagValues[w] = bestValueForWeight
    print('The optimum total value for a bag with a weight limit of', w, 'is', bagValues[w])
    print('-----------------------------------------------------------------')
    print()
