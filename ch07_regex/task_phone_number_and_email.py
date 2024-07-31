#! pythone3
#Find phone numbers and e-mail adresses on the clipboard

import pyperclip, re

#create phone regex
phone_regex = re.compile(r"""(
                         (\d{3}|\(d{3}\))?#code area
                         (\s|-|\.)?#seperator
                         (\d{3})#first 3 digits
                         (\s|-|\.)?#seperator
                         (\d{4}) #last 4 digits
                         (\s*(ext|x|ext.)\s*(\d{2,5}))?#extension
                         )""", re.VERBOSE)

#create email regex
email_regex = re.compile(r"""(
                         [a-zA-Z0-9._%+-]+#usermail
                         @#symbol
                         [a-zA-Z0-9.-]+#domain name
                         (\.[a-zA-Z] {2,4})#dot.sometging
                         
                         )""", re.VERBOSE)

#Find match in clipboard text.
text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#copy results to the clipboard
if len(matches)>0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard")
    print("\n".join(matches))

else:
    print("no phones or emails adresses found")
