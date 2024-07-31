

#setsefault
import pprint

def inventory_added(inventory_in_game):
    
    iteams_number = input("How many kind of iteams do you have?: ")

    for i in range(int(iteams_number)):
        inventory_name = input("Please, write your inventory name: ")
        inventory_count = input("Please, count your inventory, and write the number: ")
        inventory_in_game[inventory_name] = int(inventory_count)
    
    return inventory_in_game


def inventory_print (inventory_in_game):
    print()
    print("You have: ")
    for k, v in inventory_in_game.items():
        print(f"{k} : {v}")

def fight_with_dragon():
    import random
    generate_number = random.randrange(1,100)
    shoot = 0
    guess_numer = None

    print("We start the game, you have to choose 1 good number between 1:100.")
    while guess_numer != generate_number:
        guess_numer = int(input("Give it a shot: "))
        shoot += 1
        if shoot == 1:
            if guess_numer == generate_number:
                print("You have power to kill dragon in 1 shoot, congratulations you win")
                return True
            if guess_numer > generate_number: 
                print("not this way, i thing that the number is to high")
            if guess_numer < generate_number:
                print (" darling, you are too shy, the number should be bigger")
        if shoot <= 5 and shoot != 1:
            if guess_numer == generate_number:
                print(f" you have power to kill dragon in {str(shoot)} shoots,not to bad")
                return True
            if guess_numer > generate_number: 
                print(" Sorry again but not this way, i thing that the number is to high")
            if guess_numer < generate_number:
                print ("Darling not this way again, the number should be bigger, can you do it?")
        if shoot > 5 and shoot <10:
            if guess_numer == generate_number:
                print(f" Yeeee, dragon was kill in  {str(shoot)} shoots,bla bla bla,  can we go forward? mayby you should lie about this adventures.")
                return True
            if guess_numer > generate_number: 
                print("I don't know why you are here, the number is to high")
            if guess_numer < generate_number:
                print (" Darling, darling stop, not this way, the number should be bigger, can you do it?")
        if shoot >= 10:
            print("You lose, you can't kill a little dragon, take your staff from here. ")
            return False
        

           
                   
    
def dragon_loot_items(inventory_in_game):
    print("This is your awards: ")
    dragon_loot = ["gold coin", "rope", "dagger", "gold coin", "ruby"]

    for index, item in enumerate(dragon_loot):
        print(item)

    

    for index, item in enumerate(dragon_loot):
        inventory_in_game.setdefault(item, 1)

    for index, item in enumerate(dragon_loot):
        for k in inventory_in_game.keys():
            if item == k:
                inventory_in_game[k] += 1

def meet_the_dragon():
    print()
    print(" You went on your adventure, you met a dangerous dragon.")
    play = input("Play game, and fight with dragon. Do you want play YES or NO: ")
    if play == "YES":
        print()
        fight_with_dragon()
        if fight_with_dragon == True:
            dragon_loot_items(inventory_in_game)
    if play == "NO":
        print()
        print("You should come back to your mummy, if you are scary a little dragon, bring your staff and don't come back. ")
        return False
    
    

inventory_in_game = {}
inventory_added(inventory_in_game)
inventory_print(inventory_in_game)
meet_the_dragon()
inventory_print(inventory_in_game)


