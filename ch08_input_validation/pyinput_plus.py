import pyinputplus as pyip
# response = pyip.inputNum("Enter the num: ", max=4) #inputNum, max, min - value max 4 we can use int and float

# response = pyip.inputNum(blank=True) #inputNum, blank = True - no writing nothing and leave space to add num value

# response =pyip.inputNum("Enter the num with 2 limit: ", max=4, limit=2) # limit - you have only 2 shoots

# response =pyip.inputNum("Enter the num with timeout 10s: ", max=4, timeout=10)

# response = pyip.inputNum(limit=2, default='no this way')

# response = pyip.inputStr(allowRegexes=[r"catepillar", "category"], blockRegexes=[r"cat"]) #we can use pyintplus with regex 

# response = pyip.inputEmail("write your e-mail: ")

responde = pyip.inputChoice(["it not for me", "i'm in", "no no No"]) #choice one answer





