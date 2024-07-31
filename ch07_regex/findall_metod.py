# search show as a 1 result of searching
#findall return a list or if we use a () list with truple, with searched
import re

#search()
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mol = phone_num_regex.search("Cell: 415-555-9999 Work: 212-333-8888") 
print(mol.group()) # print only the 1 number

#findall()
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mol = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-333-8888") 
print(mol)
for iteam in mol:
    print (f"Find a number: {iteam}")

phone_num_regex = re.compile(r"(\d\d\d-)(\d\d\d-\d\d\d\d)") #return list with truple
mol = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-333-8888") 
print(mol)
print("Numbers below: ")
for index, iteam in enumerate(mol):
    print()
    for i in iteam:
      
      print (i, end="")

