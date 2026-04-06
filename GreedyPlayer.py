from OthelloBoardLogic import tileSwapping
import copy
import random

def greedyAlgorithm(gameBoard, playerNumber, availableMoves, totalTiles):
    initialNum = totalTiles[playerNumber]
    largestNumFlipped = -1
    bestMove = []
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
            bestMove = [(moveX, moveY)]
            largestNumFlipped = temp
        elif (temp - initialNum) == largestNumFlipped:
            bestMove.append((moveX, moveY))

    return random.choice(bestMove)
