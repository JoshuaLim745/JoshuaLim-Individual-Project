import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from OthelloGame import playTheGame, initializeGame, randomizedStartingBoard, initializeBooleans

def oneRotation(blackStrategy, whiteStrategy, loopCount):
    blackScore, whiteScore, drawScore = 0, 0, 0
    for i in range(loopCount):
        print("Game",i)
        blackWinGameOne, whiteWinGameOne, blackWinGameTwo, whiteWinGameTwo, drawGame = initializeBooleans()
        playerNumber, totalTiles, gameOngoing, gameBoard = initializeGame()

        #Randomises the starting board
        mainGameBoard, startingPlayerNumber, moveCounter, totalTiles = randomizedStartingBoard(gameBoard, totalTiles)

        firstGameBoard = [row[:] for row in mainGameBoard]
        firstTotalTiles = totalTiles[:]

        secondGameBoard = [row[:] for row in mainGameBoard]
        secondTotalTiles = totalTiles[:]

        #blackStrategy vs whiteStrategy
        score1 = playTheGame(blackStrategy, whiteStrategy, firstGameBoard, startingPlayerNumber, firstTotalTiles)
        if score1 == 1:
            blackWinGameOne = True
        elif score1 == -1:
            whiteWinGameOne = True
        else:
            drawGame = True

        #Re initialize the scores and player counts. 
        if not drawGame:
            playerNumber, totalTiles, gameOngoing, gameBoard = initializeGame()

            #whiteStrategy vs blackStrategy
            score2 = playTheGame(whiteStrategy, blackStrategy, secondGameBoard, startingPlayerNumber, secondTotalTiles)
            if score2 == 1:
                blackWinGameTwo = True
            elif score2 == -1:
                whiteWinGameTwo = True
            else:
                drawGame = True


        #blackStrategy wins on both games
        if (blackWinGameOne and whiteWinGameTwo):
            blackScore += 1

        #whiteStrategy wins on both games
        elif (whiteWinGameOne and blackWinGameTwo): 
            whiteScore += 1

        else:
            drawScore += 1

    return blackScore, whiteScore, drawScore