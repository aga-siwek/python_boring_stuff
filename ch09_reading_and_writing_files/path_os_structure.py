from pathlib import Path
import os
p = Path.cwd() / Path("ch04_list", "list.py")
chap = str(Path("ch04_list", "list.py"))

print(p.parent) #PARENT
print(p.anchor)
print(p.name)
print(p.parents[0]) #parentS
print(p.parents[1])
print(p.parents[3])


#os Dirneme and basename 

print(os.path.dirname(p))
print(os.path.basename(p))

print(os.path.split(p)) #return tuble with rest and name
print(chap.split(os. sep)) # str import,  relative 
print(str(p).split(os. sep))  # str import,  absolute

