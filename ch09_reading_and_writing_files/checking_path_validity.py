from pathlib import Path

p = Path.cwd() / Path("ch04_list", "list.py") #exsist
w = Path.cwd() / Path("ch666_list", "list.py") #no exsist
k = Path.cwd() / Path("ch04_list") #no exsist
#exists() check about exist path

print("exist")
print(p.exists())
print(w.exists())
print(k.exists())


#is file
print()
print("is file")
print(p.is_file()) #is file and exist
print(w.is_file()) #in the name is file but it no exist
print(k.is_file()) #exist but is dir

#is dir
print()
print("id dir")
print(p.is_dir()) # exist but is file
print(w.is_dir()) # no exsist
print(k.is_dir()) #exist and is dir