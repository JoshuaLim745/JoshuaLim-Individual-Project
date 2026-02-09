import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from OthelloGame import playTheGame
from RandomMove import randomMoveSelector
from GreedyPlayer import greedyAlgorithm

if __name__ == "__main__":
    playTheGame()


