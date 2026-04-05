# Game Logic functions
# Help from - https://www.youtube.com/watch?v=rvLfF9hciU8
# Link in video description of video above - https://github.com/GrizzlyH/Othello_Tutorial/blob/master/Main%205/main5.py


def directions(rowValue, colValue):
    """ Check to determine which directions are valid from current cell """
    # all cardinal and ordinal directions
    # North, South, East, West, NE, SE, NW, SW
    validDirections = []

    if rowValue != 0: 
        validDirections.append((rowValue-1, colValue))  # West
    if rowValue != 0 and colValue != 0: 
        validDirections.append((rowValue-1, colValue-1)) # SW
    if rowValue != 0 and colValue != 7: 
        validDirections.append((rowValue-1, colValue+1)) # NW

    if rowValue != 7: 
        validDirections.append((rowValue+1, colValue)) # East
    if rowValue != 7 and colValue != 0: 
        validDirections.append((rowValue+1, colValue-1)) # SE
    if rowValue != 7 and colValue != 7: 
        validDirections.append((rowValue+1, colValue+1)) # NE

    if colValue != 0: 
        validDirections.append((rowValue, colValue-1)) # South
    if colValue != 7: 
        validDirections.append((rowValue, colValue+1)) # North

    return validDirections

def findValidCells(gameBoard, playerNumber):

    """ Checks for valid cells that are adjacent / nearby to enemy cells """
    validCells = []

    for row in range(8):
        for col in range(8):

            if gameBoard[row][col] != 0:
                continue # if cell is '#' go to the next value

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