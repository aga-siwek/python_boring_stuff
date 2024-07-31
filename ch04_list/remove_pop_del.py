import random
spam = ["cat", "dog", "bat"]
print(spam)
del spam[1:3] #do 3 ale nie obejmuje 
print(spam)
spam.append("dog")
spam.append("rat")
spam.append("chicken")
spam.insert(-1, "moose")
print(spam)
spam.remove("rat")
print(spam)
spam = random.shuffle(spam)
dead_animal = spam.pop(0)
print(dead_animal)