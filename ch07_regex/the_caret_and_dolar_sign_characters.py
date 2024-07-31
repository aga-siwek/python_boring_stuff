#with search ^ sentence start on this word, $ sentence end on this word

import re
#^
print("^")
begins_with_hello = re.compile(r"^Hello") #^ after first "
mol = begins_with_hello.search("Hello my beautifull world")
print(mol.group())


begins_with_hello = re.compile(r"^Hello")
mol = begins_with_hello.search("beautifull world, Hello") #can be finded becouse it not start

if mol != None:
    print(mol.group())
else: 
    print("the word it is not on the beggining")

#$
print("$")

begins_with_hello = re.compile(r"Hello$") #^ after first "
mol = begins_with_hello.search("Hello my beautifull world")
if mol != None:
    print(mol.group())
else: 
    print("the word it is not on the end")


begins_with_hello = re.compile(r"Hello$")
mol = begins_with_hello.search("beautifull world, Hello") #can be finded becouse it not start

if mol != None:
    print(mol.group())
else: 
    print("the word it is not on the beggining")

end_with_number = re.compile(r"\d$")
mol = end_with_number.search(" Your number is 42")
print(mol.group()) #the result is 2 becouse this is the las digit)


end_with_number = re.compile(r"\d+$") # with + we have mor then 1 digit
mol = end_with_number.search(" Your number is 442")
print(mol.group()) #the result is 2 becouse this is the las digit)


#^ and $
print("^ and $")

end_with_number = re.compile(r"^\d+$") # have start and and with digit
mol = end_with_number.search("66666666442")
print(mol.group()) 




