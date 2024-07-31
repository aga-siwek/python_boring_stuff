#sub metod

import re
name_regex = re.compile(r"Agent \w+") # find Agent and next word
mol = name_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.") #sub the firs part before coma , is te word whose we will use to replace, the zesound "" it is sentence. 


print(mol)


#managing complex regexes
#VERBOSE ignore whitespace and commends, hel us to menage a very complicated code

phone_regex = re.compile(r"""
(\d{3}|\(d{3}\))? # area code
(\s|-|\.) #seperator
\d{3} #first 3 digits
(\s|-|\.) #seperator
\d{4} #last 4 digits                                                 
(\s*(ext.)\s*\d{2,5})? #extension
""", re.VERBOSE)