# [] find any letter, digit in text

import re
volves_regex = re.compile(r"[aeiouAEIOU2]")
mol = volves_regex.findall("RoboCop eats baby food. 1, 2, 3BABY FOOD")
print(mol)

# ^ not include
volves_regex = re.compile(r"[^aeiouAEIOU2]") #after [, ^ list without this
mol = volves_regex.findall("RoboCop eats baby food. 1, 2, 3BABY FOOD")
print(mol)