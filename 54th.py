import random

def game():
    print("you are playing a game....")
    score = random.randint(1,61)
# fetching the data from the hiscore.txt
    with open("hiscore.txt") as f:
         hiscore = f.read()
    if(hiscore!=""):
        hiscore = int(hiscore)
    else:
        hiscore = 0    
    print(f"your score is: {score}")

    if(score>hiscore):
         with open("hiscore.txt","w") as f:
                f.write(str(score))
                
    return score


game()