# .* replace characters without limits

#with findall
import re
name_regex = re.compile(r"First name: (.*) Last name: (.*)")
mol = name_regex.findall("First name: All Last name: Sweight")
print(mol)

#with text | greedy
name_regex = re.compile(r"First name: (.*) Last name: (.*)")
mol = name_regex.search("First name:  Last name: Sweight")
print(mol.group(1))
print(mol.group(2))

#greedy
non_greedy_regex = re.compile(r"<.*>") #for the first < to the last > all between
mo = non_greedy_regex.search("<To serve man> for dinner>")
print(mo.group())

non_greedy_regex = re.compile(r"<.*>") #for the first < to the last > all between
mo = non_greedy_regex.search("<To serve man>  \n for dinner>") # from the beggining to the new line
print(mo.group())

#nongreedy with ?, remember if you used {3,5}? you canj use it with .*

non_greedy_regex = re.compile(r"<.*?>") #for the first < to the last > all between
mo = non_greedy_regex.search("<To serve man>  \n for dinner>") # from the beggining to the new line
print(mo.group())

#will show only short <> becuse it search first >

