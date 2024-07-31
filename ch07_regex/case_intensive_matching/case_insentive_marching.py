import re
robocop_regex_1 = re.compile(r"robocop")
robocop_regex_2 = re.compile(r"robocop", re.I) #this is short cut from ignorecase, if we yse it it doesnt matter iw we use upper case or lowcase letters.
robocop_regex_3 = re.compile(r"robocop", re.IGNORECASE) 

print("mol_1")
mol_1 = robocop_regex_1.search("RoboCop is a part man, part machine, all cop.") #we kand find a result, becouse in search text we have use upper letters
if mol_1 != None:
    print(mol_1.group())
else: 
    print("We didn't find")

print("mol_2")
mol_2 = robocop_regex_2.search("RoboCop is a part man, part machine, all cop.")
if mol_2 != None:
    print(mol_2.group())
else: 
    print("We didn't find")


print("mol_3")
mol_3 = robocop_regex_3.search("RoboCoP is a part man, part machine, all cop.")
if mol_3 != None:
    print(mol_3.group())
else: 
    print("We didn't find")