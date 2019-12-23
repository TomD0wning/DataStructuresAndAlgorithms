#!/usr/bin/env python3

# Dynamic programming example for unbounded knapsack problem

# Authors: M269 Module Team
# Date: 28/8/13

# Complete the following function:
def knapsack(itemWeights, itemValues, bagWeightLimit):

    # Set up a list that will hold optimum values for weights 1 to bagWeightLimit.
    # We give index zero a dummy value for convenience (which we won't use) as we
    # want to index bagValues from 1 rather than zero.
    bagValues = [0] * (bagWeightLimit + 1)
    
    # Add your code here
    # amend the loop from Python_activity_5.9.py as specified in the activity
    
    
    # print the optimum total value for a bag of bagWeightLimit
    
    
    
# Code to test the function

# Experiment by changing the values of itemWeights, itemValues
# and bagWeightLimit to your own values. The only proviso is that
# itemWeights and itemValues must have the same number of items.

itemWeights = [12, 2, 1, 4, 1]
itemValues = [4, 2, 1, 10, 2]
bagWeightLimit = 15

knapsack(itemWeights, itemValues, bagWeightLimit)