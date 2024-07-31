#tearch and print

import re
hero_regex = re.compile(r"Batman|Tina Fey")
mol = hero_regex.search("Batman and Tina Fay, was wonderfull") # | this is or, if 2 values in text, it pruint only first
print(mol.group())

mo2 = hero_regex.search("Tina Fey and Batman")
print(mol.group())


bat_regex = re.compile(r"Bat(man|mobile|copter|wheel)")
mo = bat_regex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

#? quesion mark
print("?")
bat_regex = re.compile(r"Bat(wo)?man")
mol = bat_regex.search("We will go to adwenture with Batman and Batwoman")
print(mol.group())

bat_regex = re.compile(r"Bat(wo)?man")
mol = bat_regex.search("We will go to adwenture with Batwoman and Batman")
print(mol.group())

bat_regex = re.compile(r"Bat(wo)?man") #it can show batwowowoman becouse (wo) can be only 1 time
mol = bat_regex.search("We will go to adwenture with Batwowowoman and Batman")
print(mol.group())


#* star - can be a several time, te sentence in () in not obligatory
print("*")
bat_regex = re.compile(r"Bat(wo)*man")
mol = bat_regex.search("We will go to adwenture with Batman and Batwoman")
print(mol.group())

bat_regex = re.compile(r"Bat(wo)*man")
mol = bat_regex.search("We will go to adwenture with Batwoman and Batman")
print(mol.group())

bat_regex = re.compile(r"Bat(wo)*man")
mol = bat_regex.search("We will go to adwenture with Batwowowoman and Batman")
print(mol.group())

#+ plus the first (xx) is obligatory and can be a several time 

print("+")
bat_regex = re.compile(r"Bat(wo)+man") #the bathman in cant be show becouse it no include (wo)
mol = bat_regex.search("We will go to adwenture with Batman and Batwoman")
print(mol.group())

bat_regex = re.compile(r"Bat(wo)+man")
mol = bat_regex.search("We will go to adwenture with Batwoman and Batman")
print(mol.group())

bat_regex = re.compile(r"Bat(wo)+man")
mol = bat_regex.search("We will go to adwenture with Batwowowoman and Batman")
print(mol.group())
