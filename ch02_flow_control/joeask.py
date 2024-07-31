while True:
    print("who you are?")
    name = input()
    if name != "Joe":
        continue
    print("hello Joe, What is password? (it is a fish)")
    password = input()
    if password == "swordfish":
        break
print("access granded")