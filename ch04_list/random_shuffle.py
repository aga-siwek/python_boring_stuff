try:
    my_pets = ["Zophie", "Pooka", "Fat-tail", "Zophie"]
    print(my_pets.index("Zophie")) #show only 1 place on the lis, if we have duplicate. 
    import random
    random.shuffle(my_pets)
    print(my_pets.index("Zophie"))
    print(my_pets.index("Clara"))
except ValueError:
    print("the name in not on the pets list ")