#guess the number with limited trials

import random
import sys
guesses = 0
number = ""
print ("I am thinking of number between 1 and 20")
chosenNumber = random.randint (1,20)

for i in range(6):
    guesses += 1
    number = int(input ("Take a guess: "))
    if number > chosenNumber:
        print (" Your guess is too high")
    elif number < chosenNumber: 
        print ("Your number is to low")
    else:
        print( " Good job! You gussed my number in "+str(guesses)+" guesses")
        sys.exit()
print ("sorry you lose 6 trials")
