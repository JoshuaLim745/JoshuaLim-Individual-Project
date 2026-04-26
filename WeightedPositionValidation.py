from WeightedPosition import weightedPositionAlgorithm

Board = [
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  1, -1,  0,  0,  0],
    [ 0,  0,  1,  1, -1, -1,  0,  0],
    [ 0,  1,  1, -1,  1, -1, -1,  0],
    [ 0, -1,  1,  1, -1,  1,  1,  0],
    [ 0,  0, -1,  1, -1, -1,  0,  0],
    [ 0,  0,  0, -1,  1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0]
]

answer = weightedPositionAlgorithm(Board, -1)

print(answer)