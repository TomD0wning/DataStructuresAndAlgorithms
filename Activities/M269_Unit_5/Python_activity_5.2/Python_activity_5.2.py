#!/usr/bin/env python3

# Program to play the Grundy game between two simulated players: Alice and Bob

# Authors: M269 Module Team
# Date: 31/7/13


import random


def grundyGame(anInt):
    currentState = [anInt]
    if coinToss() == 'heads':
        toMove = 'Bob'
    else:
        toMove = 'Alice'
    over = False
    while not over:
        legalStates = getLegalStates(currentState)
        if len(legalStates) == 0:
            print(toMove, 'has no legal move left and therefore loses')
            print('*** GAME OVER ***')
            over = True
        else:
            print(toMove + "'s", 'turn,', 'legal moves are:', legalStates)
            moveResults = []
            j = 0
            for j in legalStates:
                moveResults.append(evaluateMove([j], True))
            currentState = makeMove(legalStates, moveResults, toMove)
            toMove = switchMover(toMove)


def coinToss():
    flip = random.randint(0, 1)
    if (flip == 0):
        return 'heads'
    else:
        return 'tails'


def getLegalStates(state):
    legalStates = []
    for j in range(len(state)):
        if state[j] > 2:
            for splitValue in range(1, (state[j] // 2) + 1):
                if splitValue != state[j] - splitValue:
                    newState = state[:j] + [state[j] - splitValue, splitValue] + state[j + 1:]
                    newState.sort(reverse = True)
                    if newState not in legalStates:
                        legalStates.insert(0, newState)
    return legalStates


def evaluateMove(legalStates, myMove):
    if len(legalStates) == 0:
        if not myMove:
            return ['win']
        else:
            return ['loss']
    else:
        j = 0
        moveResults = []
        while j < len(legalStates):
            successorStates = getLegalStates(legalStates[j])
            moveResults = moveResults + evaluateMove(successorStates, switchPly(myMove))
            j = j + 1
    return moveResults


def makeMove(legalStates, moveResults, toMove):
    currentState = getBestMove(legalStates, moveResults)
    print(toMove, 'moves to' , currentState)
    print()
    return currentState


def switchPly(move):
    return not move


def getBestMove(legalStates, moveResults):
    bestMove = legalStates[0]
    highestWinRatio = moveResults[0].count('win') / len(moveResults[0])
    for j in range(0, len(moveResults)):
        ratio = moveResults[j].count('win') / len(moveResults[j])
        if  ratio > highestWinRatio:
            highestWinRatio = ratio
            bestMove = legalStates[j]
    return bestMove


def switchMover(mover):
    if mover == 'Bob':
        mover = 'Alice'
    else:
        mover = 'Bob'
    return mover


grundyGame(11)
