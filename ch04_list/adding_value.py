#annding value on the end of the list
spam = ["cat", "dog", "bat"]
spam = spam + ["rat"]
print(spam)
spam += ["horse"]
print(spam)
del(spam[1])
print(spam)

spam.append("moose") #spam += ["moose"] this is she same of this line of code
print(spam)
spam.insert(1, "chicken")
print(spam)
spam.insert(-1, "dog") #IF I use insert I can add value on the end list,  
print(spam)