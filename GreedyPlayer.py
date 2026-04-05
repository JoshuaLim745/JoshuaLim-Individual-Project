from OthelloBoardLogic import tileSwapping
import copy

def greedyAlgorithm(gameBoard, playerNumber, availableMoves, totalTiles):
    initialNum = totalTiles[playerNumber]
    largestNumFlipped = -1
    bestMove = (-1,-1)
    for i in (availableMoves):
        tempBoard = copy.deepcopy(gameBoard)
        tempTiles = copy.deepcopy(totalTiles)
        moveX, moveY = i
        if (moveX, moveY) in availableMoves:
            tempBoard[moveX][moveY] = playerNumber
            tempTiles[0] += 1
            tempBoard, tempTiles = tileSwapping(tempBoard, tempTiles, moveX, moveY, playerNumber)

        temp = tempTiles[playerNumber]

        if (temp - initialNum) > largestNumFlipped:
            bestMove = (moveX, moveY)
            largestNumFlipped = temp

    return bestMove
