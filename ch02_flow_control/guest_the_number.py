import random
guesses = 0
number = ""
print ("I am thinking of number between 1 and 20")
chosenNumber = random.randint (1,20)

while number != chosenNumber:
    guesses += 1
    number = int(input ("Take a guess: "))
    if number > chosenNumber:
        print (" Your guess is too high")
    elif number < chosenNumber: 
        print ("Your number is to low")
print( " Good job! You gussed my number in "+str(guesses)+" guesses")