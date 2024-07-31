import random, sys


win = 0
losse = 0
equel = 0

while True:
   computer_choice = random.choice(["papper", "rock", "scissors"])
   my_choice = input("chose P, R, S or Q if you want exit: ")

   if my_choice == "Q" or my_choice =="q":
        sys.exit("Bay Bay")
   elif my_choice == "R" or my_choice == "r":
        if computer_choice == "rock":
            print("your move: rock, computer move: rock. equel")
            equel += 1
        elif computer_choice == "papper":
            print("your move: rock, computer move: papper. you losse")
            losse += 1
        elif computer_choice == "scissors":
            print("your move: rock, computer move: scissors. you win")
            win += 1
        print("your win: " + str(win))    
