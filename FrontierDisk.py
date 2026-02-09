directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]


def frontierCounter(gameBoard, row, col):
    for drow, dcol in directions:
        surroundingRow, surroundingCol = row + drow, col + dcol
        
        if 0 <= surroundingRow < 8 and 0 <= surroundingCol < 8:

            if gameBoard[surroundingRow][surroundingCol] == 0:
                return 1
    return 0

def frontierAlgorithm(gameBoard, playerNumber):
    opponentFrontierCount, playerFrontierCount = 0, 0

    for row in range(8):
        for col in range(8):

            if (gameBoard[row][col] == playerNumber):
                #Player's piece
                playerFrontierCount += frontierCounter(gameBoard, row, col)

            elif (gameBoard[row][col] == (-1 * playerNumber)):
                #Opponent's piece
                opponentFrontierCount += frontierCounter(gameBoard, row, col)
            else:
                continue
    
    return opponentFrontierCount - playerFrontierCount

