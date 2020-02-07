def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])



print(listSum([1,2,3,4,5]))

def move(x,y):
    print("Move {} to {}".format(x,y))


def towersOfHanoi(diskQty, fromPos, midPos, targetPos):
    if diskQty == 0:
        pass
    else:
        towersOfHanoi(diskQty-1,fromPos,targetPos,midPos)
        move(fromPos,targetPos)
        towersOfHanoi(diskQty-1,midPos,fromPos,targetPos)

towersOfHanoi(4,"A","B","C")