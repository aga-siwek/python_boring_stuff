print("Is raining? ")
RainingAnswer = input()
while RainingAnswer == "yes" or RainingAnswer =="Yes":
    print("Have a umbrela?")
    UmbrelaAnswer=input()
    while UmbrelaAnswer == "yes" or RainingAnswer =="Yes":
        print("go outsite")
        break
    else:
        print("Wait a while")
        print("Is raining? ")
        
    continue
else:
    print("go outsite")
