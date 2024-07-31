print("what your name")
name = input()
if name == "Alice":
    old = input("how old you have?")
    if int(old) > 1000:
        print ("you are wampire")
    elif int(old) > 100:
        print("you are laier, you are not this Alice")

    elif int(old)==33:
        print("welcome Alice")
    else:
        print (" maybe your name is Alice, but you are not this Alice")
else:
    print("sory, i not looking you")