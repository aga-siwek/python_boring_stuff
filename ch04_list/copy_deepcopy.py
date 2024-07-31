#copy list, diffrent ID number, if we change cheese variables we don't change spam becouse there is a diffrent list
import copy 
spam = ["A", "B", "C", "D"]
print(id(spam))
cheese = copy.copy(spam)
print(id(copy))
cheese[1] = 42
print(spam)
print(cheese)

 