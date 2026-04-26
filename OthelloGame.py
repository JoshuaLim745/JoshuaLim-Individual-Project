from RandomMove import randomMoveSelector
from GreedyPlayer import greedyAlgorithm
from AlphaBetaPruning import getBestMove
from OthelloBoardLogic import findAvaliableMoves, tileSwapping
import random

def initializeGame():
    gameOngoing = True
    playerNumber = 1 #Player with black tile starts first
    totalTiles = [4,2,2] #For score keeping and make it so that there is no need to a loop at the end to count the tiles
    """
    index 0 - Total Tiles played
    index 1 - No. Black tiles
    index 2 - No. White tiles
    """
    gameBoard = [[0]* 8 for i in range(8)]
    gameBoard[3][3] = -1
    gameBoard[3][4] = 1
    gameBoard[4][3] = 1
    gameBoard[4][4] = -1


    return (playerNumber, totalTiles, gameOngoing, gameBoard)

def randomizedStartingBoard(gameBoard, totalTiles):
    randValue = random.randint(0,6)
    playerNumber = 1
    for i in range (randValue):
        avaliableMoves = findAvaliableMoves(gameBoard, playerNumber)
        moveSelected = randomMoveSelector(avaliableMoves)


        moveX, moveY = moveSelected


        gameBoard[moveX][moveY] = playerNumber
        totalTiles[0] += 1
        gameBoard, totalTiles = tileSwapping(gameBoard, totalTiles, moveX, moveY, playerNumber)

        playerNumber *= -1
    return gameBoard, playerNumber, randValue, totalTiles

def initializeBooleans():
    blackWinGameOne, whiteWinGameOne = False, False
    blackWinGameTwo, whiteWinGameTwo = False, False
    drawGame = False

    return (blackWinGameOne, whiteWinGameOne, blackWinGameTwo, whiteWinGameTwo, drawGame)

def playTheGame(blackStrategy, whiteStrategy, gameBoard, playerNumber, totalTiles):
    passCounter = 0
    """ 
    0 - Current player has an avalible move to play
    1 - A player has to pass so allow the other player to move. Pass is occured when the current player has no possible moves to make
    2 - Both players pass so we now can end the game
    """
    gameOngoing = True
    while(gameOngoing):

        """ 
        playerNumber = 1 #Black Tile
        playerNumber = -1 #White Tile
        """
        avaliableMoves = findAvaliableMoves(gameBoard, playerNumber)
        depth = 6
        # Checks if the current player has a playable move
        if len(avaliableMoves) == 0:
            playerNumber *= -1
            passCounter += 1
        else:
            passCounter = 0
            if playerNumber == 1:
                currentPlayer = blackStrategy
            else:
                currentPlayer = whiteStrategy



            #Chooses one of the heuristics to use to select a move
            if currentPlayer == "Random":
                moveX, moveY = randomMoveSelector(avaliableMoves)

            elif currentPlayer == "Greed":
                moveX, moveY = greedyAlgorithm(gameBoard, playerNumber, avaliableMoves, totalTiles)

            elif currentPlayer == "weightedPosition":
                heuristic = "weightedPosition"
                moveX, moveY = getBestMove(gameBoard, depth, playerNumber, heuristic, avaliableMoves)

            elif currentPlayer == "Frontier":
                heuristic = "Frontier"
                moveX, moveY = getBestMove(gameBoard, depth, playerNumber, heuristic, avaliableMoves)

            if (moveX, moveY) in avaliableMoves:
                gameBoard[moveX][moveY] = playerNumber
                totalTiles[0] += 1
                gameBoard, totalTiles = tileSwapping(gameBoard, totalTiles, moveX, moveY, playerNumber)
            else:
                print("Non existent move played")

            playerNumber *= -1

        if (passCounter == 2 or totalTiles[0] >= 64):
            gameOngoing = False
            if totalTiles[1] > totalTiles[2]:
                return 1  # Black Wins
            elif totalTiles[2] > totalTiles[1]:
                return -1 # White Wins
            else:
                return 0  # Draw
