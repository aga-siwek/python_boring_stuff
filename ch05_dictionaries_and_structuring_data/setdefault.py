


#setdefault()

spam = {"name": "Pooka", "age": 5}
# if "color" not in spam:
#     spam["color"] = "black"

spam.setdefault("color", "black") # the same like a line before
spam["color"] = "yellow"
spam.setdefault("color", "black") #if color is in dict we dont change values
print(spam)