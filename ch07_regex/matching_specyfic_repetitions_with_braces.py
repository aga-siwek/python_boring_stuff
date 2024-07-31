#(Ha ){3} it mean Ha Ha Ha 
#(Ha ){3,5} it mean Ha Ha Ha or Ha Ha Ha Ha or Ha Ha Ha Ha Ha 
#(Ha ){:3} it mean Ha or Ha Ha or Ha Ha Ha
#(Ha ){3:} it mean Ha Ha Ha or more 

import re
ha_regex = re.compile(r"(Ha){3}")
mol = ha_regex.search("HaHaHa it's funny")
print(mol.group())

import re
ha_regex = re.compile(r"(Ha){3}")
mol = ha_regex.search("HaHaHaHa it's funny")
print(mol.group()) 


mol_2 = ha_regex.search("Hahaha it was funny") #it has to be exacle the same Ha with upper letter"H"
if mol_2 is not None:
    print(mol_2.group())
else:
    print("We can't find a object")

#greedy - find the longest string
greddy_ha_regex = re.compile(r"(Ha){3,5}")
mol = greddy_ha_regex.search("HaHaHaHaHa it was fun") #the longest possible
print(mol.group())

greddy_ha_regex = re.compile(r"(Ha){3,5}")
mol = greddy_ha_regex.search("HaHaHaHaHaHa it was fun") #the longest possible Ha it 5 but text include 6
print(mol.group())

#non-greedy (lazy) fin the shortest string
greddy_ha_regex = re.compile(r"(Ha){3,5}?") # ? after count
mol = greddy_ha_regex.search("HaHaHaHaHa it was fun") #the shortest possible
print(mol.group())

greddy_ha_regex = re.compile(r"(Ha){3,5}?") # ? after count
mol = greddy_ha_regex.search("HaHaHaHaHaHa it was fun") #the longest possible Ha it 3 but text include 6
print(mol.group())