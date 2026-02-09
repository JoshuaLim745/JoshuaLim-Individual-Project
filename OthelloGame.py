import os
from RandomMove import randomMoveSelector
import random


def printingBoard(gameBoard, rows):
    symbols = {1: 'b', -1: 'w', 0: '#', 9: 'A'}
    for i in range(8):
        if i == 0:
            print("", end="  ")
            print( *rows, sep = ', ')

        print(i, ", ".join(symbols[cell] for cell in gameBoard[i]))

    print()

def directions(rowValue, colValue):
    """ Check to determine which directions are valid from current cell """
    # all cardinal and ordinal directions
    # North, South, East, West, NE, SE, NW, SW
    validDirections = []

    if rowValue != 0: validDirections.append((rowValue-1, colValue))  # West
    if rowValue != 0 and colValue != 0: validDirections.append((rowValue-1, colValue-1)) # SW
    if rowValue != 0 and colValue != 7: validDirections.append((rowValue-1, colValue+1)) # NW

    if rowValue != 7: validDirections.append((rowValue+1, colValue)) # East
    if rowValue != 7 and colValue != 0: validDirections.append((rowValue+1, colValue-1)) # SE
    if rowValue != 7 and colValue != 7: validDirections.append((rowValue+1, colValue+1)) # NE

    if colValue != 0: validDirections.append((rowValue, colValue-1)) # South
    if colValue != 7: validDirections.append((rowValue, colValue+1)) # North

    return validDirections



# Game Logic functions
# Help from - https://www.youtube.com/watch?v=rvLfF9hciU8
# Link in video description of video above - https://github.com/GrizzlyH/Othello_Tutorial/blob/master/Main%205/main5.py
# https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english

def findValidCells(gameBoard, playerNumber):

    """ Checks for valid cells that are adjacent / nearby to enemy cells """
    validCells = []

    for row in range(8):
        for col in range(8):

            if gameBoard[row][col] != 0:
                continue # if cell in # go next value

            # to determine what cells are valid around a certain cell. 
            eightDirections = directions(row, col)

            for direction in eightDirections:
                xDirection, yDirection = direction
                checkedCell = gameBoard[xDirection][yDirection]

                if checkedCell == 0 or checkedCell == playerNumber:
                    continue
                
                if (row, col) in validCells:
                    continue

                validCells.append((row, col))

    return validCells

def swappableTiles(gameBoard, x, y ,playerNumber):
    surroundCells = directions(x,y)
    if len(surroundCells) == 0:
        return []
    
    swappableTiles = []

    for checkCell in surroundCells:
        checkX, checkY = checkCell
        difX , difY = checkX - x , checkY - y
        currentLine = []

        run = True

        while run:
            if gameBoard[checkX][checkY] == playerNumber * -1: # Enemy piece
                currentLine.append((checkX, checkY))

            elif gameBoard[checkX][checkY] == playerNumber: # Your own piece
                run = False
                break

            elif gameBoard[checkX][checkY] == 0: # Empty piece
                currentLine.clear()
                run = False
            
            checkX += difX
            checkY += difY


            if checkX < 0 or checkX > 7 or checkY < 0 or checkY > 7:
                currentLine.clear()
                run = False
        
        if len(currentLine) > 0:
            swappableTiles.extend(currentLine)
    return swappableTiles

def findAvaliableMoves(gameBoard, playerNumber):

    """ Takes the list of valid cells and checks for playability of that cell """

    validCells = findValidCells(gameBoard, playerNumber)

    playableCells = []

    for cell in validCells:
        x, y = cell

        if cell in playableCells:
            continue

        swapTiles = swappableTiles(gameBoard, x, y,playerNumber)
    
        if len(swapTiles) > 0:
            playableCells.append(cell)


    return playableCells





def tileSwapping(gameBoard, totalTiles, x, y, playerNumber):
    tilesToSwap = swappableTiles(gameBoard, x, y, playerNumber)
    totalTiles[playerNumber] += 1
    for tile in tilesToSwap:
        x, y = tile
        gameBoard[x][y] = playerNumber
        totalTiles[playerNumber] += 1
        totalTiles[-playerNumber] -= 1
    
    return (gameBoard, totalTiles)



def initializeGame():
    gameOngoing = True
    playerNumber = 1 #Player with black tile starts first
    totalTiles = [4,2,2] #For score keeping and make it so that there is no need to a loop at the end to count the tiles
    """
    index 0 - Total Tiles played
    index 1 - No. Black tiles
    index 2 - No. White tiles
    """
    passCounter = 0
    """ 
    0 - Current player has an avalible move to play
    1 - A player has to pass so allow the other player to move. Pass is occured when the current player has no possible moves to make
    2 - Both players pass so we now can end the game
    """
    gameBoard = [[0]* 8 for i in range(8)]
    gameBoard[3][3] = -1
    gameBoard[3][4] = 1
    gameBoard[4][3] = 1
    gameBoard[4][4] = -1
    rows = [ f'{i}' for i in range(8)]

    return (playerNumber, totalTiles, passCounter, gameBoard, rows, gameOngoing)

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



def playTheGame():
    playerNumber, totalTiles, passCounter, gameBoard, rows, gameOngoing = initializeGame()
    gameBoard, playerNumber, moveCounter, totalTiles = randomizedStartingBoard(gameBoard, totalTiles)
    while(gameOngoing):


        """ 
        playerNumber = 1 #Black Tile
        playerNumber = -1 #White Tile
        """
        avaliableMoves = findAvaliableMoves(gameBoard, playerNumber)

        # Checks if the current player has a playable move
        if len(avaliableMoves) == 0:
            playerNumber *= -1
            passCounter += 1
        else:
            #Removing terminal clutter 
            os.system('cls' if os.name == 'nt' else 'clear')

            if moveCounter % 2 == 0:
                print("Move ", moveCounter,":Black Move")
            else:
                print("Move ", moveCounter,":White Move")

            passCounter = 0
            # Just to display the current playable moves. Can delete if needed to. 
            printingBoard(gameBoard, rows)
            print(avaliableMoves, "\n")

            # Taking user input - Will eventually be swapped out with some getMove from a class. 
            userX = int(input("Move in the X coordinate \n"))
            userY = int(input("Move in the Y coordinate \n"))

            if (userX, userY) in avaliableMoves:
                gameBoard[userX][userY] = playerNumber
                totalTiles[0] += 1
                gameBoard, totalTiles = tileSwapping(gameBoard, totalTiles, userX, userY, playerNumber)
            else:
                print("Not valid move")
            printingBoard(gameBoard, rows)
            playerNumber *= -1


                                                                    #Change the greater than or equal to also
        if (passCounter == 2 or totalTiles[0] >= 64 ) : 
            gameOngoing = False
        
        moveCounter += 1

    print("Total Tiles in play: ",totalTiles[0], "\n")
    print("Total Black Tiles in play: ",totalTiles[1], "\n")
    print("Total White Tiles in play: ",totalTiles[2], "\n")

    if(totalTiles[1] > totalTiles[2]):
        print("Black Wins", "\n")
    elif (totalTiles[1] < totalTiles[2]):
        print("White Wins", "\n")
    else:
        print("Draw", "\n")








#if __name__ == "__main__":
#    playTheGame()