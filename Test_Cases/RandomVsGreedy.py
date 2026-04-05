from OneRotation import oneRotation
import random
blackStrategy = "Random"
whiteStrategy = "Greed"

randomScore, greedScore, drawScore = 0, 0, 0
random.seed("JoshuaLim")

if __name__ == "__main__":
    randomScore, greedScore, drawScore = oneRotation("Random", "Greed", 100)

    print(randomScore)
    print(greedScore)
    print(drawScore)