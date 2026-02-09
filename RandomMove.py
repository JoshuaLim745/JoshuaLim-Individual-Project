import random
def randomMoveSelector(listOfMoves):
    moveToPlay = random.sample(listOfMoves, 1)
    
    return moveToPlay[0]
