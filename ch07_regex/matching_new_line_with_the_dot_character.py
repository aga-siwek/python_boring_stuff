import re

no_new_line_regex = re.compile(".*")
mol = no_new_line_regex.search("Serve the public trust \n Protect the innocent") #print to the new line
print(mol.group())


new_line_regex = re.compile(".*", re.DOTALL) #if we wan to use .* include new line we should use re.DOTALL fuction after , 
mol = new_line_regex.search("Serve the public trust \n Protect the innocent.\n Thats vision on perfect world") #print to the new line
print(mol.group())