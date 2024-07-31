import random
import sys

wins = 0
losses = 0
ties = 0
# 1 rock, 2 papper, 3 scissors
while True:
    oponentAnswer = input("Enter your move: (r)ock, (p)apper, (s)cissors or (q)uick: ")
    computerAnswer = random.randint(1,3)
    if oponentAnswer == "q":
        sys.exit("bye")
    elif computerAnswer == 1 and oponentAnswer == "r":
        print ("ROCK")
        print ("vs Rock")
        print ("This is a tie!")
        ties += 1
    elif computerAnswer == 1 and oponentAnswer == "p":
        print ("PAPPER")
        print ("vs Rock")
        print ("You win")  
        wins += 1
    elif computerAnswer == 1 and oponentAnswer == "s":
        print ("SCISSORS")
        print ("vs Rock")
        print ("You lose")  
        losses += 1

    elif computerAnswer == 2 and oponentAnswer == "r":
        print ("ROCK")
        print ("vs Papper")
        print ("You lose")  
        losses += 1
    elif computerAnswer == 2 and oponentAnswer == "p":
        print ("PAPPER")
        print ("vs Papper")
        print ("This is a tie!")  
        ties += 1
    elif computerAnswer == 2 and oponentAnswer == "s":
        wins += 1
        print ("SCISSORS")
        print ("vs Papper")
        print ("You win!")  
        wins += 1
    elif computerAnswer == 3 and oponentAnswer == "r":
        print ("ROCK")
        print ("vs Scissors")
        print ("You win!")
        wins += 1
    elif computerAnswer ==3 and oponentAnswer == "p":
        print ("PAPPER")
        print ("vs Scissors")
        print ("You lose!")
        losses += 1
    elif computerAnswer == 3 and oponentAnswer == "s":
        print ("SCISSORS")
        print ("vs Scissors")
        print ("This is a tie!")
        ties += 1
        
    print("wins: " +str(wins) + ", losses: " + str(losses) + ", ties: "+ str(ties))
    
