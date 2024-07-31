# \d any numeric digit from 0-9
# \d+ any numeric digit ones or more for example 1 or 12
# \D without numeric digit
# \w any letter or numeric digit or underscore character_ ones
# \w+ any letter or numeric digit or underscore character_ ones or more time
# \W with out any letter or numeric digit or underscore character_
# \s any space tab or new line 
# \S with out any space tab or new line 

import re

x_mas_regex = re.compile(r"\d+\s\w+")
mol = x_mas_regex.findall(" 12 drummers, 11 pipers, 10 lords, 9 ladis, 8 maids, 7 swan") 
print(mol)

 