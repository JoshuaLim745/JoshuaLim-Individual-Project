from OneRotation import oneRotation
import random
import time

strategyList = ["Random", "Greed", "Corner", "Frontier"]

drawScore, blackStrategyScore, whiteStrategyScore = 0, 0, 0
random.seed("JoshuaLimYonJian")

if __name__ == "__main__":
    startTime = time.time()

    for blackStrategy in strategyList:
        for whiteStrategy in strategyList:
            blackStrategyScore, whiteStrategyScore, drawScore = oneRotation(blackStrategy, whiteStrategy, 100)


            print("Black Strategy:", blackStrategy)
            print("Black Win Score:", blackStrategyScore)

            print("-" * 15)
            print("White Strategy:", whiteStrategy)
            print("White Win Score:", whiteStrategyScore)

            print("-" * 15)
            print("Draw Score:", drawScore)
            print("-" * 15)

            print()
            print()

    endTime = time.time()

    print("Time Taken:", (endTime - startTime))