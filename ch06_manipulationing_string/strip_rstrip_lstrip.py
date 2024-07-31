#removing whitecharacters(space, tab newline etc)
#strip() from beggining and end
#rstrip()from the right site
#lstriop() from the lefi site 



spam = """   hello


"""

print(spam)
print(5 * "-")
print(spam.strip())
print(5 * "-")
print(spam.lstrip())
print(5 * "-")
print(spam.rstrip())

#we can remove specyfic characters
spam="hello"
print("2")
print(spam)
print(5 * "-")
print(spam.strip("h"))
print(5 * "-")
print(spam.lstrip("h"))
print(5 * "-")
print(spam.rstrip("h"))