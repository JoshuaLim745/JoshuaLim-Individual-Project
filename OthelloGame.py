#Global variables
gameOngoing = True
playerTurn = True
gameBoard = [[0]* 8 for i in range(8)]

gameBoard[3][3] = 1
gameBoard[3][4] = -1
gameBoard[4][3] = -1
gameBoard[4][4] = 1
rows = [ f'{i}' for i in range(8)]


# General Functions
def printingBoard():
    symbols = {1: 'b', -1: 'w', 0: '#', 9: 'A'}
    for i in range(8):
        if i == 0:
            print(" ", end="  ")
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

def findValidCells(playerNumber):

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

def swappableTiles(x, y ,playerNumber):
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

def findAvaliableMoves(playerNumber):

    """ Takes the list of valid cells and checks for playability of that cell """

    validCells = findValidCells(playerNumber)

    playableCells = []

    for cell in validCells:
        x, y = cell

        if cell in playableCells:
            continue

        swapTiles = swappableTiles(x, y,playerNumber)
    
        if len(swapTiles) > 0:
            playableCells.append(cell)


    return playableCells

# The game code itself / main


    """ 
    TODO: 
    Possible ideas is to just keep an internal track of this
    so just flip flop between w -> b -> w -> b

    The only case where this breaks is when one player has no possible move to make
    Which is where this function could be called and used to enforce the flip flop. 
    """


while(gameOngoing):

    if playerTurn == True:
        playerNumber = 1
    else:
        playerNumber = -1

    avaliableMoves = findAvaliableMoves(playerNumber)

    if len(avaliableMoves) == 0:
        playerTurn = not(playerTurn)
        continue
    else:
        playerTurn = not(playerTurn)
        

        for playableMoves in avaliableMoves:
            x, y = playableMoves
            gameBoard[x][y] = 9
        printingBoard()

        userX = int(input("Move in the X coordinate \n"))
        userY = int(input("Move in the Y coordinate \n"))
        printingBoard()
        userAnswer = 'n'
        if userAnswer == 'n':
            gameOngoing = False




