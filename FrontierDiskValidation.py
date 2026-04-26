from FrontierDisk import frontierAlgorithm

# Known board obtained from https://reversi-othello-en.blogspot.com/2011/10/frontier-disc-and-walls.html

# Black has 12 frontier disk.
# White has  2 frontier disk.
# Program is expected to return -10 when given playerNumber  = 1.
# If playerNumber = -1 --> the score return would be 10
# Because if the score given to the current player is negative the current is the worse position.
# This means that white(-1) is in the better position here

Board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,-1, 1, 1, 1,0,0],
    [0,0, 1,-1, 1, 1,0,0],
    [0,0, 1, 1,-1, 1,1,0],
    [0,0, 1, 1, 1,-1,0,0],
    [0,0,0 , 1,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

answer = frontierAlgorithm(Board, -1)

print(answer)