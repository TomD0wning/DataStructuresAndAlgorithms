#!/usr/bin/env python3

# Dynamic programming solution for the Levenshtein Edit Distance problem.

# Authors: M269 Module Team
# Date: 30/08/13


# Function used to 'pretty print' results conveniently
def printTable(table):
    for row in table:
        for item in row:
            print(str(item).ljust(2), end=' ')
        print()

def diff(a, b):
    if a == b:
        return 0
    else:
        return 1

# This is the function that does all the work
# The code has been extensively modified from the algorithm as given in the unit
# in order to explain the workings of the algorithm step by step and display the
# populated table in the correct format.
# You do not need to understand the detailed working of this implementation:
# the point of the activity is to run the program with the example strings to
# observe the progress of the algorithm and the end result.
def editDistance(str1, str2):
    x = str1
    y = str2
    m = len(x)
    n = len(y)

    # Set up table of zeros
    e = [[0 for i in range(m + 1)] for j in range(n + 1)]


    # Put initial values in borders
    for i in range(0, n + 1):
        e[i][0] = i
    for j in range(0, m + 1):
        e[0][j] = j

    # the entries of table f will hold I, D, R or O according to
    # what is the last move to achieve the minimum number of moves given by
    # the corresponding entry in e. This will enable the actual
    # intermediate stages to be displayed in going from str1 to
    # str2
    f = [['' for i in range(m + 1)] for j in range(n + 1)]
    # put required directions in borders
    f[0] = ['D' for i in range(m + 1)]
    for i in range(n + 1):
        f[i][0]='I'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # insertion, deletion, match/mismatch
            a = 1 + e[i - 1][j] # for insertion
            b = 1 + e[i][j - 1] # for deletion
            d = diff(x[j - 1], y[i - 1]) # distinguishes insertion from replacement
            c = d + e[i - 1][j - 1] # for insertion and replacement

            # the minimum of a, b, c tells us where we came from
            if (c < a) & (c < b):
                if d != 0:
                    f[i][j] = 'R'
                else:
                    f[i][j] = 'O'
            else:
                if b < a:
                    f[i][j] = 'D'
                else:
                    f[i][j] = 'I'
            e[i][j]= min(1 + e[i - 1][j], 1 + e[i][j - 1], diff(x[j - 1], y[i - 1]) + e[i - 1][j - 1])

    # The elements of move will hold the type of move and the string that results
    # For now move is simply filled with spaces
    move = [[' ' for i in range(2)] for j in range(e[i][j] + 1)]

    # start at the end of each string
    i = len(y)
    j = len(x)
    pos = e[i][j] # we start at the end (after last move)
    move[0][0] = 'Start  :' # move[0][1] will be the start string once we get there
    move[pos][1] = y # this is the finish string
    while pos > 0:
        current = f[i][j] # how we got here

        if current == 'I':
            move[pos][0] = 'Insert :'
            pos = pos - 1
            i = i - 1 # move back in the string y
            # to get the previous string delete the character that was inserted
            move[pos][1] = move[pos + 1][1][:i] + move[pos + 1][1][i + 1:]

        else:
            if current == 'O':
                # the current characters matched so move back in both x and y
                i = i - 1
                j = j - 1

            else:
                if current == 'D':
                    move[pos][0] = 'Delete :'
                    pos = pos - 1
                    j = j - 1 # move back in string x
                    # to get the previous string insert the character that was deleted from x
                    move[pos][1] = move[pos + 1][1][:i] + x[j] + move[pos + 1][1][i:]

                else: ## must be an R
                    move[pos][0] = 'Replace:'
                    pos = pos - 1
                    # move back in both string x and y
                    i = i - 1
                    j = j - 1
                    # to get the previous string replace the original character from x
                    move[pos][1] = move[pos + 1][1][:i] + x[j] + move[pos + 1][1][i + 1:]

    return e, move

def runEditDist(str1, str2):
    e, w = editDistance(str1, str2)
    print(str1, 'to', str2, 'in', e[len(str2)][len(str1)], 'moves')
    printTable(w)
    printTable(e)
    print()


runEditDist('TREES', 'FOREST')
runEditDist('POLYNOMIAL', 'EXPONENTIAL')
runEditDist('KITTEN', 'SITTING')
runEditDist('SITTING', 'KITTEN')
runEditDist('SIX', 'ELEVEN')
