from OneRotation import oneRotation
import random
import time

strategyList = ["Random", "Greed", "Corner", "Frontier"]

drawScore, blackStrategyScore, whiteStrategyScore = 0, 0, 0
random.seed("JoshuaLimYon")

if __name__ == "__main__":

    for blackStrategy in strategyList:
        for whiteStrategy in strategyList:
            startTime = time.time()
            blackStrategyScore, whiteStrategyScore, drawScore = oneRotation(blackStrategy, whiteStrategy, 50)


            with open("smallScale.txt", "a") as f:
                print("Black Strategy:", blackStrategy, file=f)
                print("Black Win Score:", blackStrategyScore, file=f)

                print("-" * 15, file=f)
                print("White Strategy:", whiteStrategy, file=f)
                print("White Win Score:", whiteStrategyScore, file=f)

                print("-" * 15, file=f)
                print("Draw Score:", drawScore, file=f)
                print("-" * 15, file=f)
                
                endTime = time.time()
                print("Time Taken:", (endTime - startTime), file=f)
                print("-" * 15, file=f)

                
                print("\n", file=f)
