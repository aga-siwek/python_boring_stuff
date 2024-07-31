my_pets = ["Zophie", "Pooka", "Fat-tail"]
name = input("Enter a pet name: ")
if name not in my_pets:
    print("do you not have pet name: " + name)
else:
    print (name + " is my pet")