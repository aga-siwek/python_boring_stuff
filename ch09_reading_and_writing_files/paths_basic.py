from pathlib import Path
p = Path("spam", "becon", "eggs")
print(str(p))

o = Path("spam") / "bacon" / "egg" #check on mac

print(str(o))
print (Path.cwd())

print (Path.cwd().is_absolute())

p = Path.cwd() / Path("ch04_list", "list.py")
print(type(p))
print(p.is_absolute())


import os

#abspath - print a string

print(os.path.abspath(Path.cwd() / Path("ch04_list", "list.py")))


#os relpath = return relative

print(os.path.relpath("D:\programowanie\python_automate_boring_stuff\ch04_list\list.py", "list")) #path, start

#os isabs 

print(os.path.isabs("D:\programowanie\python_automate_boring_stuff\ch04_list\list.py"))



