from OthelloBoardLogic import findAvaliableMoves, tileSwapping
from FrontierDisk import frontierAlgorithm
from WeightedPosition import weightedPositionAlgorithm
import random

# https://www.geeksforgeeks.org/dsa/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

def alphaBetaPruning(gameBoard, depth, alpha, beta, maximizingPlayer, playerNumber, heuristic, originalPlayerNumber):
    avaliableMoves = findAvaliableMoves(gameBoard, playerNumber)

    if depth == 0:
        if heuristic == "Frontier":
            return frontierAlgorithm(gameBoard, originalPlayerNumber)
        
        elif heuristic =="weightedPosition":
            return weightedPositionAlgorithm(gameBoard, originalPlayerNumber)
    
    if not avaliableMoves:
        opponentMoves = findAvaliableMoves(gameBoard, -playerNumber)
        if not opponentMoves: 
            # No player has a move
            if heuristic == "Frontier":
                return frontierAlgorithm(gameBoard, originalPlayerNumber)
            
            elif heuristic =="weightedPosition":
                return weightedPositionAlgorithm(gameBoard, originalPlayerNumber)
        # Current player has no moves, but opponent does.
        # We update playerNumber and maximizingPlayer accodingly
        return alphaBetaPruning(gameBoard, depth-1, alpha, beta, not maximizingPlayer, -playerNumber, heuristic, originalPlayerNumber)


    if maximizingPlayer:
        bestValue = float("-inf")

        for move in avaliableMoves:
            tempBoard = [row[:] for row in gameBoard]
            moveX, moveY = move
            tempBoard, ignoreValues = tileSwapping(tempBoard, [0,0,0], moveX, moveY, playerNumber)
            bestValue =  max(bestValue, alphaBetaPruning(tempBoard, depth-1, alpha, beta, False, -playerNumber, heuristic, originalPlayerNumber))

            if bestValue >= beta:
                break

            alpha = max(alpha, bestValue)
        
        return bestValue

    else:

        minValue = float("inf")

        for move in avaliableMoves:
            tempBoard = [row[:] for row in gameBoard]
            moveX, moveY = move
            tempBoard, ignoreValues = tileSwapping(tempBoard, [0,0,0], moveX, moveY, playerNumber)
            minValue =  min(minValue, alphaBetaPruning(tempBoard, depth-1, alpha, beta, True, -playerNumber, heuristic, originalPlayerNumber))

            if minValue <= alpha:
                break

            beta = min(beta, minValue)
        
        return minValue
    

def getBestMove(gameBoard, depth, playerNumber, heuristic, avaliableMoves):

    if not avaliableMoves:
        return None

    bestMoves = []
    alpha = float("-inf")
    originalPlayerNumber = playerNumber
    for move in avaliableMoves:
        tempBoard = [row[:] for row in gameBoard]
        tempTiles = [0,0,0]
        moveX, moveY = move
        tempBoard, tempTiles = tileSwapping(tempBoard, tempTiles, moveX, moveY, playerNumber)
        
        boardValue = alphaBetaPruning(tempBoard, depth-1, alpha, float("inf"), False, -playerNumber, heuristic, originalPlayerNumber)
        
        if boardValue > alpha:
            alpha = boardValue
            bestMoves = [move]
        elif boardValue == alpha:
            bestMoves.append(move)

    if bestMoves:
        return random.choice(bestMoves)
    
    else:
        return None
    