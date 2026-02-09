import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from OthelloGame import playTheGame, initializeGame, randomizedStartingBoard, initializeBooleans

blackStrategy = "Random"
whiteStrategy = "Greed"

randomScore, greedScore, drawScore = 0, 0, 0


if __name__ == "__main__":
    for i in range(1000):

        blackWinGameOne, whiteWinGameOne, blackWinGameTwo, whiteWinGameTwo, drawGame = initializeBooleans()
        playerNumber, totalTiles, gameOngoing, gameBoard = initializeGame()

        #Randomises the starting board
        mainGameBoard, playerNumber, moveCounter, totalTiles = randomizedStartingBoard(gameBoard, totalTiles)

        firstGameBoard = [row[:] for row in gameBoard]
        firstTotalTiles = totalTiles[:]

        secondGameBoard = [row[:] for row in gameBoard]
        secondTotalTiles = totalTiles[:]

        #Random(black) vs Greed(white)
        score1 = playTheGame(blackStrategy, whiteStrategy, firstGameBoard, playerNumber, moveCounter, firstTotalTiles)
        if score1 == 1:
            blackWinGameOne = True
        elif score1 == -1:
            whiteWinGameOne = True
        else:
            drawGame = True

        #Re initialize the scores and player counts. 
        if not drawGame:
            ingoreVariable, totalTiles, gameOngoing, gameBoard = initializeGame()
            #Greed(black) vs Random(white)
            score2 = playTheGame(whiteStrategy, blackStrategy, secondGameBoard, playerNumber, moveCounter, secondTotalTiles)
            if score2 == 1:
                blackWinGameTwo = True
            elif score2 == -1:
                whiteWinGameTwo = True
            else:
                drawGame = True


        #Random wins on both black (game 1) and white (game 2)
        if (blackWinGameOne and whiteWinGameTwo):
            randomScore += 1
        #Greed wins on both white (game 1) and black (game 2)
        elif (whiteWinGameOne and blackWinGameTwo): 
            greedScore += 1
        else:
            drawScore += 1

    print(randomScore)
    print(greedScore)
    print(drawScore)