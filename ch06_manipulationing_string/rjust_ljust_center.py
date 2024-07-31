#rjust(10) ten spaces from text + spaces from rught site = 10 characters
#ljust(10) spaces + tekst from left site = 10 characters
#center(10) center text and spaces from left and right 

spam = "Hello World"
print(spam.ljust(15))
print(spam.rjust(15))
print(spam.center(15))

print(spam.ljust(15,"*"))
print(spam.rjust(15, "%"))  #you can use only 1 character after comma
print(spam.center(15, "#"))