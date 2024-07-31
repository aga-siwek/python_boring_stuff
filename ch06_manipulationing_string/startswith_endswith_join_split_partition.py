spam = "I invaite you to my little green hause, I have: "
print(spam.startswith("I"))
print(spam.endswith("hause"))

spam_2 = ["cat", "rat", "dog"]
print(", ".join(spam_2)) #return str
print("ABC".join(spam_2)) #return str
print(spam_2)

spam_3 ="MyABCNameABCIsABCAga"
print(spam_3.split("ABC")) # return list
spam_3 ="dog, cats, rabbits"
print(spam_3.split(", "))
print(spam_3)
spam_3 = spam_3.split(", ")
print(spam_3)

spam_4 = """
Dear Alice,
How have you been? I am fine.
There is a container in the fridge
That is "labeled Milk Experiment".

Please do not drink it.
Sincererly, 
Bob

"""
print(spam_4)
spam_4 = spam_4.split("\n") #split return to the list, we seperated when been enter.
print(spam_4)

#partition split the text and leave the splited part

spam_3 ="MyABCNameABCIsABCAga"
print(spam_3.split("ABC")) #create list, remove ABC in whole sentence ['My', 'Name', 'Is', 'Aga']
print(spam_3.partition("ABC")) # create 3 part of text, before seperator, seperator, after seperator, firt ABC to seperate and rest leave create Truple ('My', 'ABC', 'NameABCIsABCAga')
before, sep, after = spam_3.partition("ABC")
print(before)
print(sep)
print(after)

