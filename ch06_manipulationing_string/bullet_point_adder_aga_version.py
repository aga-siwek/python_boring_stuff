#! python3
import pyperclip
previous_text = pyperclip.paste()
previous_list = previous_text.split("\n")
for index, iteam in enumerate(previous_list):
   previous_list[index] = "*" + previous_list[index]

list = "\n".join(previous_list) #jon to change list to str
print("text is prepare to paste")
pyperclip.copy(list) #we cant copy a list

