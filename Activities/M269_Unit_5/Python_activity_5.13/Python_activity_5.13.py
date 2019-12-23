#!/usr/bin/env python3

# Implementation of the MINIMAX algorithm for an abstract game

# Authors: M269 Module Team
# Date: 8/10/13

from pythonds.trees import GeneralTree


# Create and populate gameTree - only the leaf nodes are given non-zero payloads.
# The program calculates the minimax values for other nodes as it executes. The
# calculated minimax values of non leaf nodes is not used to update their payloads.

gameTree = GeneralTree('S1', 0)
gameTree.insertChildOf('S1', 'S2', 0)
gameTree.insertChildOf('S1', 'S3', 0)
gameTree.insertChildOf('S1', 'S4', 0)
gameTree.insertChildOf('S2', 'S5', 0)
gameTree.insertChildOf('S2', 'S6', 0)
gameTree.insertChildOf('S2', 'S7', 0)
gameTree.insertChildOf('S3', 'S8', 0)
gameTree.insertChildOf('S3', 'S9', 0)
gameTree.insertChildOf('S4', 'S10', 0)
gameTree.insertChildOf('S4', 'S11', 0)
gameTree.insertChildOf('S5', 'S12', 7)
gameTree.insertChildOf('S5', 'S13', 6)
gameTree.insertChildOf('S6', 'S14', 8)
gameTree.insertChildOf('S6', 'S15', 5)
gameTree.insertChildOf('S7', 'S16', 2)
gameTree.insertChildOf('S7', 'S17', 3)
gameTree.insertChildOf('S8', 'S18', 0)
gameTree.insertChildOf('S8', 'S19', -2)
gameTree.insertChildOf('S9', 'S20', 6)
gameTree.insertChildOf('S9', 'S21', 2)
gameTree.insertChildOf('S10', 'S22', 5)
gameTree.insertChildOf('S10', 'S23', 8)
gameTree.insertChildOf('S11', 'S24', 9)
gameTree.insertChildOf('S11', 'S25', 2)

# Set up global variables
currentState = gameTree.getRoot()
maxPlyDepth = 3
currentPlayer = 'Maximiser'
callNumber = 0

def abstractGameMinimax():
    print()
    print('>>>Inside abstractGameMinimax()')
    legalMoves = currentState.getChildren()
    if len(legalMoves) == 0:
        print(currentPlayer, ' has no legal move and loses')
        print('===== END OF GAME =====')
        return
    else :
        print('  ', currentPlayer, 'to move from', currentState.getKey(), '-', 'evaluating best move out of:', end='')
        for node in legalMoves:
            print('   ', node.getKey(), end='')
        print()
        minmaxValues = collectMinimaxValues(legalMoves)
        print()
        print('<<<Back inside abstractGameMinimax()')
        print('Minimax values for legal moves: ',  end='')
        printMinimaxString(legalMoves, minmaxValues)
        print()
        makeMove(legalMoves, minmaxValues)
        print()
        print('<<<Back inside abstractGameMinimax()')
        print('*******************NEXT PLAYER\'S TURN************************')
        #Recursive call follows
        #abstractGameMinimax()



# Helper funtion for printing states and minimax values
def printMinimaxString(legalMoves, minmaxValues):
    for i in range(len(legalMoves) - 1):
        print(legalMoves[i].getKey(), '(', minmaxValues[i], '), ', sep='', end='')
    print(legalMoves[len(legalMoves) - 1].getKey(), '(', minmaxValues[len(legalMoves) - 1], ')', sep='', end='')



def collectMinimaxValues(legalMoves):
    print()
    print('>>>Inside collectMinimaxValues()')
    minimaxValues = []
    nextPlayer = switchMover(currentPlayer)
    for node in legalMoves:
        print('   Evaluating move to', node.getKey(), 'for', currentPlayer)
        print('')
        mmValue = getMinimaxValue(node, nextPlayer, 1)
        print()
        print('<<<Back inside collectMinimaxValues()')
        print('   Appending', mmValue, 'to minimaxValues')
        minimaxValues.append(mmValue)
    return minimaxValues


def getMinimaxValue(aNode, aPlayer, ply):
    global callNumber
    callNumber = callNumber + 1
    localCall = callNumber
    indent = '   ' * ply
    print(indent, '>>>Inside call', localCall, 'of getMinimaxValue()')
    print(indent, '   Calculating', aPlayer, 'minimax value for', aNode.getKey(), 'at ply', ply)
    minimaxValue = 0
    successorStates = aNode.getChildren()
    if len(successorStates) == 0:
        #We've reached a leaf node
        minimaxValue = aNode.getPayload()
    elif ply == maxPlyDepth:
        #With our sample game tree, this branch only executes if maxPlyDepth < 3
        minimaxValue = aNode.getPayload()
    else:
        #Temporarily switch players to see what the next player's move would be
        #if they were in the successorState. This doesn't effect the global variable currentPlayer
        nextPlayer = switchMover(aPlayer)
        minMaxList = []
        for state in successorStates:
            #Recursive call follows
            print(indent, '   Making recursive call of getMinimaxValue()')
            print()
            aValue = getMinimaxValue(state, nextPlayer, ply + 1)
            print()
            print(indent, '<<<Back inside call', localCall, 'of getMinimaxValue()')
            print(indent, '   Appending', aValue, 'to', 'minimaxList')
            minMaxList.append(aValue)
        if aPlayer == 'Maximiser':
            minimaxValue = max(minMaxList)
        else:
            minimaxValue = min(minMaxList)
    print('  ', indent, aPlayer, 'minimax value of', aNode.getKey(), 'is', minimaxValue)
    return minimaxValue


def makeMove(legalMoves, moveResults):
    global currentState
    global currentPlayer
    print()
    print('>>>Inside makeMove()')
    if currentPlayer == 'Minimiser':
        bestMoveIndex = min(moveResults)
    else:
        bestMoveIndex = max(moveResults)
    #Change global variable
    currentState = legalMoves[moveResults.index(bestMoveIndex)]
    print(currentPlayer, 'moves to', currentState.getKey())
    #Change global variable
    currentPlayer = switchMover(currentPlayer)


def switchMover(aPlayer):
    if aPlayer == 'Minimiser':
        return 'Maximiser'
    else:
        return 'Minimiser'


print('-------------------------MiniMax-------------------------')

abstractGameMinimax()
