from OthelloBoardLogic import findAvaliableMoves, tileSwapping
from FrontierDisk import frontierAlgorithm
import copy

# https://www.geeksforgeeks.org/dsa/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# set alpha to -inf and beta to inf, maximizingPlayer = true
def AlphaBetaPruning(gameBoard, depth, alpha, beta, maximizingPlayer, playerNumber, heuristic):
    avaliableMoves = findAvaliableMoves(gameBoard, playerNumber)
    if depth == 0 or not avaliableMoves:
        if heuristic == "Frontier":
            return frontierAlgorithm(gameBoard, playerNumber)
        else:
            return 0


    if maximizingPlayer:
        bestValue = float("-inf")

        for move in avaliableMoves:
            tempBoard = [row[:] for row in gameBoard]
            tempTiles = [0,0,0]
            moveX, moveY = move
            tempBoard, tempTiles = tileSwapping(tempBoard, tempTiles, moveX, moveY, playerNumber)
            bestValue =  max(bestValue, AlphaBetaPruning(tempBoard, depth-1, alpha, beta, False, playerNumber, heuristic))

            if bestValue >= beta:
                break

            alpha = max(alpha, bestValue)
        
        return bestValue

    else:

        minValue = float("inf")

        for move in avaliableMoves:
            tempBoard = [row[:] for row in gameBoard]
            tempTiles = [0,0,0]
            moveX, moveY = move
            tempBoard, tempTiles = tileSwapping(tempBoard, tempTiles, moveX, moveY, playerNumber)
            minValue =  min(minValue, AlphaBetaPruning(tempBoard, depth-1, alpha, beta, True, playerNumber, heuristic))

            if minValue <= alpha:
                break

            beta = min(beta, minValue)
        
        return minValue
    

def getBestMove(gameBoard, depth, playerNumber, heuristic):
    availableMoves = findAvaliableMoves(gameBoard, playerNumber)
    if not availableMoves:
        return None
    
    bestMove = None
    bestValue = float("-inf")
    
    for move in availableMoves:
        tempBoard = [row[:] for row in gameBoard]
        tempTiles = [0,0,0]
        moveX, moveY = move
        tempBoard, tempTiles = tileSwapping(tempBoard, tempTiles, moveX, moveY, playerNumber)
        
        boardValue = AlphaBetaPruning(tempBoard, depth-1, float("-inf"), float("inf"), False, playerNumber, heuristic)
        
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
            
    return bestMove